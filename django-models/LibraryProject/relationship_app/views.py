from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

#listing all books stored in the database
def book_list(request):
    return render(request, 'relationship_app/list_books.html' , Book.objects.all())

#listing all books available in a library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['libray_books'] = library.books.all()
        return context