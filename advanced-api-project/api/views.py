from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# BookListView
# GET → Retrieve all books
# Anyone (authenticated or not) can access this view.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# BookDetailView
# GET → Retrieve a single book by ID
# Accessible to everyone.
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# BookCreateView
# POST → Create a new book
# Only authenticated users can create books.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save()


# BookUpdateView
# PUT / PATCH → Update an existing book
# Only authenticated users can update books.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# BookDeleteView
# DELETE → Remove a book
# Only authenticated users can delete books.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]