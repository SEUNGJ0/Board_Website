# Generated by Django 4.0.6 on 2022-08-20 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Files', '0012_alter_errorlog_error_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errorlog',
            name='error_message',
            field=models.JSONField(default=dict),
        ),
    ]