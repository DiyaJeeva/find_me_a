# Generated by Django 3.2.7 on 2022-02-04 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindMeA', '0002_interest_interest_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interest',
            name='username',
        ),
        migrations.RemoveField(
            model_name='interest',
            name='users',
        ),
        migrations.AlterField(
            model_name='interest',
            name='interest_text',
            field=models.CharField(max_length=200),
        ),
    ]
