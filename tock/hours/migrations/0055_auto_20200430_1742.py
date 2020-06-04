# Generated by Django 2.2.12 on 2020-04-30 21:42

from django.db import migrations, models
import django.db.models.deletion
from django.core.exceptions import ObjectDoesNotExist

def backfill_timecard_organization_and_unit(apps, schema_editor):
    Timecard = apps.get_model('hours', 'Timecard')
    UserData = apps.get_model('employees', 'UserData')

    for timecard in Timecard.objects.all():
        try:
            user_data = UserData.objects.get(user=timecard.user)
            timecard.organization = user_data.organization
            timecard.unit = user_data.unit
            timecard.save()
        except ObjectDoesNotExist:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0006_unit_initial_data'),
        ('hours', '0054_auto_20200423_1523'),
        ('employees', '0028_remove_userdata_is_billable')
    ]

    operations = [
        migrations.AddField(
            model_name='timecard',
            name='organization',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.Organization'),
        ),
        migrations.AddField(
            model_name='timecard',
            name='unit',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.Unit'),
        ),
        migrations.RunPython(backfill_timecard_organization_and_unit)
    ]