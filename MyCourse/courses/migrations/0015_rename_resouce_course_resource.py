# Generated by Django 4.1.3 on 2022-12-03 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_alter_payment_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='resouce',
            new_name='resource',
        ),
    ]
