from django.urls import path

from books.views import AddBook, BookDetail, BookListView, EditBook

urlpatterns = [
    path("", BookListView.as_view(), name="books_list"),
    path("books/add_book", AddBook.as_view(), name="add_book"),
    path("books/<int:pk>/", BookDetail.as_view(), name="books_detail"),
    path("books/<int:pk>/edit", EditBook.as_view(), name="edit_book"),
]
