# Joining the Tock team

[:arrow_left: Back to Tock
Documentation](https://github.com/18F/tock/tree/master/docs)

## Onboarding

When you join the Tock team, you may be expected to complete the following
onboarding checklist on with minimal guidance. The Tock Product Owner may
schedule check-in time with you to ensure that you're progressing and aren't
stuck. If there is another Tock developer already on the project, you will be
assigned them as a buddy to help you progress through onboarding.

## Checklist

Create a new issue with the following checklist. Swapping out {TockDeveloper}
with the name of the onboarding developer.

- [ ] {TockDeveloper} has access to New Relic
- [ ] {TockDeveloper} has access to GitHub repository
- [ ] {TockDeveloper} has access to SpaceDeveloper roles in Cloud Foundry for
  spaces `staging` and `prod`.
- [ ] {TockDeveloper} is invited to #tock-dev in Slack
- [ ] {TockDeveloper} is familiar with the [deployment process of
  Tock](https://github.com/18f/tock/tree/master/docs/deployment-process.md)


## Things we maintain

- [Tock](tock-app), a Python Django framework web application comprised of multiple
  sub-apps.
  - tock - The main application
  - employees - The application that manages the employee data
  - projects - The application that manages the project data
  - hours - The application that manages the hours and reporting data
  - organizations - The application that manages organizations
  - api - The application that manages the API
  - utilization - The application that manages the utilization functionality
- [AngryTock](tock-bot), a Golang Slack RTM-based bot
- [#tock-dev](tock-chat), a Slack channel where Tock users come for technical
  support.

[tock-app]: https://github.com/18F/tock
[tock-bot]: https://github.com/18F/angrytock
[tock-chat]: https://gsa-tts.slack.com/messages/C1JFYCX3P

### Important terminology and context

- [cloud.gov][docs-cg] - The PaaS that Tock uses to deploy all the apps
- [Postgres][docs-psql] - The database backend that the Tock application uses
- [Python][docs-python] - The language that the Tock app uses
- [Golang][docs-golang ]- The language that the AngryTock Slack bot uses
- [Django Web Framework][docs-django] - The application framework that the Tock application is
  built with.
- [Django Rest Framework][docs-django-rest] - The REST framework that the Tock
  application is built with.
- [Slack Real-Time Messaging (RTM) API][docs-slack-rtm] - The Slack API that AngryTock uses to
  communicate via Slack
- [cloud.gov identity provider][docs-cg-idp] - The identity provider that Tock
  uses for user authentication.
- [cloud.gov service account][docs-cg-sa] - The service account that Tock uses
  for deployments.
- [cloud.gov UAA authentication backend][docs-django-uaa] - The UAA client that
  the Tock application uses to leverage the cloud.gov identity provider.

[docs-cg]: https://cloud.gov/docs/
[docs-cg-idp]: https://cloud.gov/docs/services/cloud-gov-identity-provider/
[docs-cg-sa]: https://cloud.gov/docs/services/cloud-gov-service-account/
[docs-psql]: https://www.postgresql.org/docs/
[docs-python]: https://docs.python.org/3/
[docs-golang]: https://golang.org/doc/
[docs-django]: https://docs.djangoproject.com/en/1.11/
[docs-django-rest]: http://www.django-rest-framework.org
[docs-django-uaa]: http://cg-django-uaa.readthedocs.io/en/latest/
[docs-slack-rtm]: https://api.slack.com/rtm