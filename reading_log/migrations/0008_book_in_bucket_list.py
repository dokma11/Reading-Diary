# Generated by Django 4.2.6 on 2023-10-09 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reading_log', '0007_book_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='in_bucket_list',
            field=models.BooleanField(default=False),
        ),
    ]
