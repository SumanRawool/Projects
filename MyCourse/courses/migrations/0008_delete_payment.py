# Generated by Django 4.1.3 on 2022-11-30 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_usercourse_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
