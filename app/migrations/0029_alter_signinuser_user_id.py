# Generated by Django 5.0.4 on 2024-04-12 06:14

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_alter_leg_mkt_price_alter_signinuser_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signinuser',
            name='user_id',
            field=models.CharField(default=app.models.generate_uuid_pattern, max_length=100),
        ),
    ]
