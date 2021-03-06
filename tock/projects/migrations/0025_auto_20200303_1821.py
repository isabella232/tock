# Generated by Django 2.2.10 on 2020-03-03 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0024_project_exclude_from_billability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='notes_displayed',
            field=models.BooleanField(default=False, help_text='Check this if a notes field should be displayed along with a time entry against a project.', verbose_name='Notes are requested (not required)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='notes_required',
            field=models.BooleanField(default=False, help_text='Check if notes should be required for time entries against this project. Note: Checking this enables notes display as well.', verbose_name='Notes are required'),
        ),
    ]
