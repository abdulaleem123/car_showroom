# Generated by Django 4.2.7 on 2023-12-01 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(default='', upload_to='cars/images'),
        ),
    ]
