# Generated by Django 4.1.3 on 2022-11-15 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
