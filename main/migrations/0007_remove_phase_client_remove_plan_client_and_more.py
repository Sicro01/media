# Generated by Django 4.0.6 on 2022-08-01 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_clientplan_plan_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phase',
            name='client',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='client',
        ),
        migrations.RemoveField(
            model_name='strategy',
            name='phase',
        ),
    ]
