# Generated by Django 3.2.7 on 2022-02-11 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FindMeA', '0004_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='phone_numer',
        ),
    ]
