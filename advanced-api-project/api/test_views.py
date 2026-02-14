from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(TestCase):
    """Unit tests for Book API endpoints."""

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create books
        self.book1 = Book.objects.create(title="Book One", publication_year=2000, author=self.author1)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2010, author=self.author2)

        # Setup API client
        self.client = APIClient()

   
    # Test List View
    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Two books created


    # Test Detail View
    def test_get_book_detail(self):
        response = self.client.get(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Book One")

    # Test Create Book
    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        data = {
            "title": "Book Three",
            "publication_year": 2022,
            "author": self.author1.id
        }
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "Book Three")

    def test_create_book_unauthenticated(self):
        data = {
            "title": "Book Four",
            "publication_year": 2022,
            "author": self.author1.id
        }
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Test Update Book
    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        data = {
            "title": "Updated Book One",
            "publication_year": 2001,
            "author": self.author1.id
        }
        response = self.client.put(f'/api/books/update/{self.book1.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book One")


    # Test Delete Book
    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(f'/api/books/delete/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())


    # Test Filtering / Search / Ordering
    def test_filter_books_by_author(self):
        response = self.client.get(f'/api/books/?author={self.author1.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book One")

    def test_search_books_by_title(self):
        response = self.client.get('/api/books/?search=Two')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book Two")

    def test_order_books_by_publication_year_desc(self):
        response = self.client.get('/api/books/?ordering=-publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2010)