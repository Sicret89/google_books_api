# Generated by Django 4.0.1 on 2022-01-23 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_remove_book_cover_link_book_book_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_link',
            new_name='link',
        ),
    ]
