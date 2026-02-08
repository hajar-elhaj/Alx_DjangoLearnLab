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

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer


# List books with filtering, searching, and ordering
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    # Step 1: Filtering
    filterset_fields = ['title', 'publication_year', 'author']

    # Step 2: Search
    search_fields = ['title', 'author__name']

    # Step 3: Ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering
