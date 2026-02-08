from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Author, Book


class BookAPITests(APITestCase):
    """
    Test suite for Book API endpoints.
    Covers CRUD operations, permissions, filtering, searching, and ordering.
    """

    def setUp(self):
        """
        Set up test data before each test runs.
        """
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        self.author = Author.objects.create(name="George Orwell")

        self.book1 = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )

        self.book2 = Book.objects.create(
            title="Animal Farm",
            publication_year=1945,
            author=self.author
        )

        self.book_list_url = "/books/"
        self.book_detail_url = f"/books/{self.book1.id}/"

    # ---------- READ TESTS ----------

    def test_get_book_list(self):
        """
        Unauthenticated users should be able to retrieve book list.
        """
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_book_detail(self):
        """
        Unauthenticated users should be able to retrieve a single book.
        """
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "1984")

    # ---------- CREATE TESTS ----------

    def test_create_book_requires_authentication(self):
        """
        Unauthenticated users should NOT be able to create a book.
        """
        data = {
            "title": "Homage to Catalonia",
            "publication_year": 1938,
            "author": self.author.id
        }
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_create_book(self):
        """
        Authenticated users should be able to create a book.
        """
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "Homage to Catalonia",
            "publication_year": 1938,
            "author": self.author.id
        }

        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # ---------- UPDATE TESTS ----------

    def test_update_book_authenticated(self):
        """
        Authenticated users should be able to update a book.
        """
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "Nineteen Eighty-Four",
            "publication_year": 1949,
            "author": self.author.id
        }

        response = self.client.put(self.book_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Nineteen Eighty-Four")

    # ---------- DELETE TESTS ----------

    def test_delete_book_authenticated(self):
        """
        Authenticated users should be able to delete a book.
        """
        self.client.login(username="testuser", password="testpassword")

        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ---------- FILTER / SEARCH / ORDER TESTS ----------

    def test_filter_books_by_publication_year(self):
        """
        Test filtering books by publication year.
        """
        response = self.client.get("/books/?publication_year=1945")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Animal Farm")

    def test_search_books_by_title(self):
        """
        Test searching books by title.
        """
        response = self.client.get("/books/?search=1984")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_publication_year(self):
        """
        Test ordering books by publication year.
        """
        response = self.client.get("/books/?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Animal Farm")
