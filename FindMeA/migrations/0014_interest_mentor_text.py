# Generated by Django 3.2.7 on 2022-02-19 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindMeA', '0013_rename_mentor_subject_userprofile_mentor_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='interest',
            name='mentor_text',
            field=models.CharField(default='Not Applicable', max_length=200),
        ),
    ]
