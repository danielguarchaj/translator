# Generated by Django 3.1.2 on 2020-10-28 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0007_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='translation',
            name='user_age',
            field=models.IntegerField(default=0),
        ),
    ]