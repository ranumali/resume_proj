# Generated by Django 4.2.4 on 2023-09-18 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0006_rename_about_my_resume_about1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='my_resume',
            old_name='about1',
            new_name='about_1',
        ),
        migrations.RenameField(
            model_name='my_resume',
            old_name='githubid',
            new_name='about_2',
        ),
        migrations.RenameField(
            model_name='my_resume',
            old_name='university',
            new_name='clg_name',
        ),
        migrations.RenameField(
            model_name='my_resume',
            old_name='company_name',
            new_name='company_name_1',
        ),
        migrations.RenameField(
            model_name='my_resume',
            old_name='designation1',
            new_name='company_name_2',
        ),
        migrations.RenameField(
            model_name='my_resume',
            old_name='working_years',
            new_name='designation_1',
        ),
        migrations.RenameField(
            model_name='my_resume',
            old_name='linkedinid',
            new_name='github_id',
        ),
        migrations.RenameField(
            model_name='my_resume',
            old_name='mobile_no',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='my_resume',
            old_name='years_graduation',
            new_name='years_degree',
        ),
        migrations.AddField(
            model_name='my_resume',
            name='designation_2',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='my_resume',
            name='linkedin_id',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='my_resume',
            name='working_years_1',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='my_resume',
            name='working_years_2',
            field=models.CharField(default=11, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='my_resume',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='my_resume',
            name='percent_1',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='my_resume',
            name='percentage_1',
            field=models.CharField(max_length=70),
        ),
    ]
