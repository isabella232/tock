import datetime

from django.contrib.auth import get_user_model
from django.urls import reverse
from django_webtest import WebTest
from employees.models import UserData
from hours.models import ReportingPeriod, Timecard, TimecardObject
from organizations.models import Organization, Unit
from projects.models import AccountingCode, Agency, Project

User = get_user_model()

FIXTURES = [
    'tock/fixtures/prod_user.json',
    'projects/fixtures/projects.json',
    'hours/fixtures/timecards.json',
    'employees/fixtures/user_data.json',
]


class TestGroupUtilizationView(WebTest):
    fixtures = [
        'projects/fixtures/projects.json',
    ]

    def setUp(self):
        # Create non-billable and billable accounting codes
        # Create Timecard populated with project lines
        billable_acct = AccountingCode.objects.create(
            code='foo',
            billable=True,
            agency=Agency.objects.first()
        )

        non_billable_acct = AccountingCode.objects.create(
            code='foo',
            billable=False,
            agency=Agency.objects.first()
        )

        # Grab projects to associate with the account codes
        non_billable_project = Project.objects.first()
        non_billable_project.accounting_code = non_billable_acct
        non_billable_project.save()

        billable_project = Project.objects.last()
        billable_project.accounting_code = billable_acct
        billable_project.save()

        test_org = Organization.objects.get_or_create(id=1)[0]
        test_unit = Unit.objects.get_or_create(org=test_org)[0]

        self.user = User.objects.create(
            username='regular.user',
            is_staff=True
        )
        # When we create the user, we have to assign them a unit from test data
        # or else we can't find them in test data.
        self.user_data = UserData.objects.get_or_create(user=self.user)[0]
        self.user_data.unit = test_unit
        self.user_data.save()

        self.reporting_period = ReportingPeriod.objects.create(
            start_date=datetime.date(2015, 10, 1),
            end_date=datetime.date(2015, 10, 7)
        )
        self.timecard = Timecard.objects.create(
            reporting_period=self.reporting_period,
            user=self.user,
            submitted=True
        )

        self.nb_timecard_object = TimecardObject.objects.create(
            timecard=self.timecard,
            project=non_billable_project,
            hours_spent=15,
        )

        self.b_timecard_object = TimecardObject.objects.create(
            timecard=self.timecard,
            project=billable_project,
            hours_spent=25,
        )

        # Save timecard to calculate utilization
        self.timecard.save()

    def test_summary_rows(self):
        """
        Row data w/ accurate total present in context
        for user created in setup
        """
        response = self.app.get(
            url=reverse('utilization:GroupUtilizationView'),
            user=self.user
        )
        utilization_data = response.context['object_list'][0]['utilization']

        self.assertEqual(
            utilization_data['last_week_data'][0]['total'],
            (self.b_timecard_object.hours_spent + \
            self.nb_timecard_object.hours_spent)
        )

        self.assertEqual(
            utilization_data['last_week_data'][0]['billable'],
            self.b_timecard_object.hours_spent
        )
