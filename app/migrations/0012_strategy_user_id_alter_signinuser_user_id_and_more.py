# Generated by Django 5.0.3 on 2024-03-29 07:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_signinuser_user_id_alter_strategy_strategy_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='strategy',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.signinuser'),
        ),
        migrations.AlterField(
            model_name='signinuser',
            name='user_id',
            field=models.CharField(default='9149146063447891160111', max_length=100),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='strategy_id',
            field=models.CharField(default='5CD583888400677319193', max_length=100),
        ),
    ]
