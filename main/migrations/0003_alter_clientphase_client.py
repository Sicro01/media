# Generated by Django 4.0.6 on 2022-07-31 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_clientplan_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientphase',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.client'),
        ),
    ]
