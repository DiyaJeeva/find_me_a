# Generated by Django 3.2.7 on 2022-04-08 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindMeA', '0018_auto_20220308_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.TextField(default='', max_length=500),
        ),
    ]