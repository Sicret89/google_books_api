# Generated by Django 4.0.1 on 2022-02-01 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_remove_book_category_remove_book_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn_number',
            field=models.CharField(blank=True, default=None, max_length=13, null=True, unique=True),
        ),
    ]
