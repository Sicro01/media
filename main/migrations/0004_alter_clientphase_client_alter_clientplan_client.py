# Generated by Django 4.0.6 on 2022-08-01 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_clientphase_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientphase',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phases', to='main.client'),
        ),
        migrations.AlterField(
            model_name='clientplan',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='main.client'),
        ),
    ]
