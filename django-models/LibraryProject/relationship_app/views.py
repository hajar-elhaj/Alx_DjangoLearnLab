from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView

#listing all books stored in the database
def list_books(request):
    books = Book.objects.all()                 # fetch all books
    context = {'books': books}                 # wrap it in a dictionary
    return render(request, 'relationship_app/list_books.html', context)


#listing all books available in a library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['libray_books'] = library.books.all()
        return context
    
# Registration view
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')  # redirect after successful registration

# Login view
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout view
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'  
    next_page = '/login/'  # optional redirect after logout                 