# Generated by Django 2.2.12 on 2020-06-04 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0033_auto_20200515_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.Organization'),
        ),
    ]