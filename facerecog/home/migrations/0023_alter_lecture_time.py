# Generated by Django 4.0.3 on 2022-08-24 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_alter_lecture_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='time',
            field=models.TimeField(),
        ),
    ]
