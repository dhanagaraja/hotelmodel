# Generated by Django 4.2.9 on 2024-02-07 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_alter_staff_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='image',
            field=models.ImageField(default='media/default.jpg', upload_to='', verbose_name='Photo'),
        ),
    ]
