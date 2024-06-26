# Generated by Django 5.0.3 on 2024-04-02 04:09

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_signinuser_user_id_alter_strategy_strategy_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signinuser',
            name='user_id',
            field=models.CharField(default='7D070402105534178175698659', max_length=100),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='strategy_id',
            field=models.CharField(default=app.models.strategy_uuid, max_length=100, unique=True),
        ),
    ]
