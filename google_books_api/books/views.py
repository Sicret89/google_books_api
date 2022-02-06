from datetime import datetime
from itertools import chain

from django.shortcuts import redirect, render
from django.views.generic import ListView

from .forms import BookSearchForm
from .models import Book


class BookListView(ListView):

    model = Book
    template_name = "books/books_list.html"
    paginate_by = 15
    form_class = BookSearchForm

    def get_queryset(self):
        title = self.request.GET.get("title", "")
        author = self.request.GET.get("author", "")
        publication_language = self.request.GET.get("publication_language", "").lower()
        publication_date_start = self.request.GET.get("publication_date_start", "")
        publication_date_end = self.request.GET.get("publication_date_end", "")
        filters = []
        if not any([title, author, publication_language, publication_date_start, publication_date_end]):
            return self.model.objects.all()
        if author:
            by_author = self.model.objects.filter(author__icontains=author)
            filters.append(by_author)
        if title:
            by_title = self.model.objects.filter(title__icontains=title)
            filters.append(by_title)
        if publication_language:
            by_lang = self.model.objects.filter(publication_language__icontains=publication_language)
            filters.append(by_lang)
        if publication_date_start:
            publication_date_start = datetime.strptime(publication_date_start, "%Y-%m-%d").date()
            by_publication_date_start = self.model.objects.filter(published_date__gte=publication_date_start)
            filters.append(by_publication_date_start)
        if publication_date_end:
            publication_date_end = datetime.strptime(publication_date_end, "%Y-%m-%d").date()
            by_publication_date_end = self.model.objects.filter(published_date__lte=publication_date_end)
            filters.append(by_publication_date_end)
        books_list = list(chain(*filters))
        return books_list
