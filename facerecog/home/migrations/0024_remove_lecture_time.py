# Generated by Django 4.0.3 on 2022-08-24 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_alter_lecture_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='time',
        ),
    ]
