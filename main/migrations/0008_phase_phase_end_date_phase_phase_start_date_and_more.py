# Generated by Django 4.0.6 on 2022-08-01 16:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_phase_client_remove_plan_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='phase',
            name='phase_end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='phase',
            name='phase_start_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='plan',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.client'),
        ),
        migrations.AddField(
            model_name='plan',
            name='phase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.phase'),
        ),
        migrations.AddField(
            model_name='plan',
            name='strategy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.strategy'),
        ),
        migrations.AddField(
            model_name='strategy',
            name='strategy_end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='strategy',
            name='strategy_start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
