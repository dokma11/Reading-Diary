# Generated by Django 4.2.6 on 2023-10-07 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reading_log', '0003_book_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name_plural': 'reviews'},
        ),
    ]
