# Generated by Django 4.0.6 on 2022-08-01 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_clientphase_phase'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClientPlan',
            new_name='Plan',
        ),
        migrations.RenameModel(
            old_name='ClientStrategy',
            new_name='Strategy',
        ),
    ]