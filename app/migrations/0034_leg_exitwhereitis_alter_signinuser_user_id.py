# Generated by Django 5.0.4 on 2024-04-16 05:41

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_leg_stop_trigger_flag_alter_signinuser_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='leg',
            name='exitwhereitis',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='signinuser',
            name='user_id',
            field=models.CharField(default=app.models.generate_uuid_pattern, max_length=100),
        ),
    ]
