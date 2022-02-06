import re
import sys
from datetime import datetime
from itertools import chain

import requests
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView, UpdateView, View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter

from .forms import BookAddForm, BookSearchForm, ImportBooksForm
from .models import Book
from .serializers import BookSerializer


class BookListView(ListView):
    """
    View responsible for listing Book objects.
    """

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


class ListBookAPIView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["title", "author", "isbn_number", "published_date"]
    search_fields = ["title", "author", "isbn_number", "published_date"]


class AddBook(SuccessMessageMixin, CreateView):
    """
    View responsible for adding Book objects.
    """

    model = Book
    template_name = "books/add_book.html"
    success_message = "Your book has been Created!"
    form_class = BookAddForm


class BookDetail(DetailView):
    """
    View responsible for displaying Book detail.
    """

    model = Book
    template_name = "books/books_detail.html"


class EditBook(SuccessMessageMixin, UpdateView):
    """
    View responsible for editing Book objects.
    """

    model = Book
    template_name = "books/edit_book.html"
    success_message = "Your book has been Edited!"
    form_class = BookAddForm


class GoogleBooksImport(View):
    """
    View responsible for adding Book objects from Google API.
    """

    model = Book

    def get(self, request):
        form = ImportBooksForm()
        return render(request, "books/import_books.html", {"form": form})

    def get_clean_authors_list(self, authors):
        if isinstance(authors, list):
            return ", ".join([item for item in authors])
        return authors

    def get_clean_isbn(self, identifiers_list):
        if identifiers_list:
            if isbn_list := [item for item in identifiers_list if item.get("type") == "ISBN_13"]:
                return isbn_list[0].get("identifier")
        return None

    def get_clean_date(self, pub_date):
        if pub_date:
            if re.match(r"^\d{4}-+\d{2}-+\d{2}", pub_date):
                return pub_date

    def post(self, request):
        form = ImportBooksForm(request.POST)
        if form.is_valid():
            query = request.POST["query"]
            try:
                r = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={query}")
                if r.status_code == 200:
                    result = r.json()
                    for item in result["items"]:
                        if Book.objects.filter(title=item["volumeInfo"]["title"]):
                            messages.warning(
                                request,
                                f"Books with '{query}'\
                                 key already existing in database.",
                            )
                            return render(request, "books/import_books.html", {"form": form})
                        else:
                            if "authors" in item["volumeInfo"]:
                                book = Book()
                                book.title = item["volumeInfo"]["title"]
                                for item in result["items"]:
                                    volume_info = item["volumeInfo"]
                                    book_info = {
                                        "title": volume_info.get("title"),
                                        "author": self.get_clean_authors_list(volume_info.get("authors")),
                                        "published_date": self.get_clean_date(volume_info.get("publishedDate")),
                                        "isbn_number": self.get_clean_isbn(volume_info.get("industryIdentifiers")),
                                        "page_count": volume_info.get("pageCount"),
                                        "publication_language": volume_info.get("language"),
                                    }
                                    if volume_info.get("imageLinks") is not None:
                                        book_info["image_link"] = volume_info.get("imageLinks").get("thumbnail")
                                    else:
                                        book_info["image_link"] = None
                                    book, _ = Book.objects.update_or_create(**book_info)
                                    book.save()
                            messages.success(request, "Your books have been imported from Google API")
                            return redirect("books_list")
            except ConnectionError as e:
                print(e, file=sys.stderr)
                messages.warning(request, "Error, Can not connect to the API.")
                print("Error, Can not connect to the API.")
                exit()
                return render(request, "books/import_books.html", {"form": form})
