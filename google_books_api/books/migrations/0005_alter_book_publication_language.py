# Generated by Django 4.0.1 on 2022-01-23 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_options_remove_book_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_language',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
