# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-29 20:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0024_auto_20171229_1156'),
        ('projects', '0023_auto_20171229_1156'),
        ('hours', '0034_auto_20171229_1156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timecardprefilldata',
            options={'verbose_name': 'Timecard Prefill Data', 'verbose_name_plural': 'Timecard Prefill Data'},
        ),
        migrations.AddField(
            model_name='timecardprefilldata',
            name='employee',
            field=models.ForeignKey(default='1234', on_delete=django.db.models.deletion.CASCADE, related_name='timecard_prefill_data', to='employees.UserData'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='timecardprefilldata',
            unique_together=set([('employee', 'project')]),
        ),
    ]