# Generated by Django 2.2.13 on 2020-06-23 16:29

from django.db import migrations, models

def make_default_utilization(apps, schema_editor):
    Projects = apps.get_model('projects','Project')

    for project in Projects.objects.all():
        project.include_in_utilization = project.is_billable
        project.save()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0026_auto_20200519_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='include_in_utilization',
            field=models.BooleanField(default=False, help_text='For handling microrequests, per github.com/18F/tock/issues/1084'),
        ),
    migrations.RunPython(make_default_utilization) 
    ]
