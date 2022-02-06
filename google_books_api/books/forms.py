from django import forms


class BookSearchForm(forms.Form):
    """
    Form for searching books in books_list view.
    """

    title = forms.CharField(max_length=150, required=False)
    author = forms.CharField(max_length=150, required=False)
    published_date_start = forms.DateField(required=False)
    published_date_end = forms.DateField(required=False)
    publication_language = forms.CharField(max_length=150, required=False)
