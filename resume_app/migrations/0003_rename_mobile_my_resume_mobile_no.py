# Generated by Django 4.2.4 on 2023-09-15 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0002_my_resume_delete_myprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='my_resume',
            old_name='mobile',
            new_name='mobile_no',
        ),
    ]
