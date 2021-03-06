# Generated by Django 4.0.1 on 2022-01-23 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_genre_alter_book_options_remove_book_authors_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={},
        ),
        migrations.RemoveField(
            model_name='book',
            name='description',
        ),
        migrations.RemoveField(
            model_name='book',
            name='genres',
        ),
        migrations.RemoveField(
            model_name='book',
            name='name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='price',
        ),
        migrations.AddField(
            model_name='book',
            name='cover_link',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='number_of_pages',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='publication_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='publication_language',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
