# Generated by Django 5.0.3 on 2024-04-01 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_signinuser_user_id_alter_strategy_strategy_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signinuser',
            name='user_id',
            field=models.CharField(default='CC2206359624769540415981', max_length=100),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='strategy_id',
            field=models.CharField(default='STA05F6EC4', max_length=100),
        ),
    ]
