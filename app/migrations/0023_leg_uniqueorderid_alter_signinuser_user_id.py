# Generated by Django 5.0.3 on 2024-04-02 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_rename_status_strategy_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leg',
            name='uniqueorderid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='signinuser',
            name='user_id',
            field=models.CharField(default='0710710102448383966615', max_length=100),
        ),
    ]
