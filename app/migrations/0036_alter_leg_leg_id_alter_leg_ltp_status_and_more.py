# Generated by Django 5.0.4 on 2024-04-17 06:12

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_leg_leg_id_alter_signinuser_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leg',
            name='leg_id',
            field=models.CharField(blank=True, default=app.models.leg_uuid, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='leg',
            name='ltp_status',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='signinuser',
            name='user_id',
            field=models.CharField(default=app.models.generate_uuid_pattern, max_length=100),
        ),
    ]