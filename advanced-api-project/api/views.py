"""
BookListView supports advanced query capabilities:
- Filtering by title, author, and publication_year
- Searching by title and author name
- Ordering by title and publication_year
Query examples:
    /api/books/?search=harry
    /api/books/?publication_year=2020
    /api/books/?ordering=-publication_year
"""

from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filterset_fields = ['title', 'publication_year', 'author']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']
