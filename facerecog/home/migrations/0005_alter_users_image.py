# Generated by Django 4.0.3 on 2022-04-27 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_users_date_users_degree_users_email_users_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
