# Generated by Django 4.0.3 on 2022-05-27 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_lecture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecture',
            old_name='Lecture_id',
            new_name='lecture_id',
        ),
    ]
