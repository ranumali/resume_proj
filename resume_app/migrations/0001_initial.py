# Generated by Django 4.2.4 on 2023-09-13 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fathername', models.CharField(max_length=50)),
                ('mothername', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('roll_no', models.IntegerField()),
                ('stream', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('pin_code', models.CharField(max_length=6)),
                ('gender', models.CharField(max_length=50)),
                ('mobile_no', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='media')),
                ('description', models.CharField(max_length=400)),
            ],
        ),
    ]
