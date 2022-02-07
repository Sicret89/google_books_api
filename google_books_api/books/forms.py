from django import forms

from .models import Book


class BookSearchForm(forms.Form):
    """
    Form for searching books in books_list view.
    """

    title = forms.CharField(max_length=150, required=False)
    author = forms.CharField(max_length=150, required=False)
    published_date_start = forms.DateField(required=False)
    published_date_end = forms.DateField(required=False)
    publication_language = forms.CharField(max_length=150, required=False)


class BookAddForm(forms.ModelForm):
    """
    Form for adding books in add_book view
    """

    published_date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}), required=True)

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


class ImportBooksForm(forms.Form):
    """
    Form for adding books form google.
    """

    query = forms.CharField(label="Enter Keywords", max_length=100, required=False)
