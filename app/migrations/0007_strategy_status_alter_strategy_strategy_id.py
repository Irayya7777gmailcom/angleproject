# Generated by Django 5.0.3 on 2024-03-27 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_leg_id_alter_strategy_strategy_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='strategy',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='strategy_id',
            field=models.CharField(default='3B1319326394208679205240940', max_length=100),
        ),
    ]
