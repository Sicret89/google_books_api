from django.test import TestCase

from books.models import Book


class BookModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Book.objects.create(
            title="title test",
            author="author test",
            published_date="2020-06-06",
            isbn_number=1112223334445,
            page_count=350,
            image_link="http://test.com/",
            publication_language="en",
        )

    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "title")

    def test_isbn_number_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("isbn_number").verbose_name
        self.assertEqual(field_label, "isbn number")

    def test_author_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("author").verbose_name
        self.assertEqual(field_label, "author")

    def test_published_date_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("published_date").verbose_name
        self.assertEqual(field_label, "published date")

    def test_page_count_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("page_count").verbose_name
        self.assertEqual(field_label, "page count")

    def test_image_link_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("image_link").verbose_name
        self.assertEqual(field_label, "image link")

    def test_publication_language_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("publication_language").verbose_name
        self.assertEqual(field_label, "publication language")

    def test_title_max_length(self) -> None:
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field("title").max_length
        self.assertEqual(max_length, 150)

    def test_isbn_number_max_length(self) -> None:
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field("isbn_number").max_length
        self.assertEqual(max_length, 13)

    def test_publication_language_max_length(self) -> None:
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field("publication_language").max_length
        self.assertEqual(max_length, 150)

    def test_string_representation_title(self) -> None:
        book = Book.objects.get(id=1)
        expected_obj_name = f"{book.title}"
        self.assertEqual(str(book), expected_obj_name)
