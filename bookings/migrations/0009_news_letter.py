# Generated by Django 4.2.9 on 2024-02-08 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0008_booking_adult_booking_child'),
    ]

    operations = [
        migrations.CreateModel(
            name='News_Letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'News Letter',
                'verbose_name_plural': 'News Letters',
                'db_table': 'news_letter',
            },
        ),
    ]