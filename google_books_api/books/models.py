from django.db import models
from django.urls import reverse


class Book(models.Model):

    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150, null=True, default=None, blank=True)
    published_date = models.DateField(null=True, default=None, blank=True)
    isbn_number = models.CharField(max_length=13, null=True, default=None, blank=True, unique=True)
    page_count = models.IntegerField(null=True, default=None, blank=True)
    image_link = models.URLField(max_length=500, null=True, default=None, blank=True)
    publication_language = models.CharField(max_length=150, null=True, default=None, blank=True)

    def get_absolute_url(self) -> str:
        """
        Retrieves url to self
        :return: Url to self resource.
        """
        return reverse("books_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("title",)
