# Generated by Django 4.0.3 on 2022-08-25 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_alter_lecture_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
