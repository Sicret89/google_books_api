from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for REST Book model.
    """

    class Meta:
        model = Book
        fields = (
            "title",
            "author",
            "published_date",
            "isbn_number",
            "page_count",
            "image_link",
            "publication_language",
        )
