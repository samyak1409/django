# Generated by Django 4.1.7 on 2023-02-24 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(default='Profile Pics/Default.jpg', upload_to='Profile Pics'),
        ),
    ]
