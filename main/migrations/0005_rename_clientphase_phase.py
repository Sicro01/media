# Generated by Django 4.0.6 on 2022-08-01 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_clientphase_client_alter_clientplan_client'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClientPhase',
            new_name='Phase',
        ),
    ]
