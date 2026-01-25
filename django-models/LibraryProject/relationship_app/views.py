from django.shortcuts import render , redirect
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User


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
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redirect to login page after registration
    else:
        form = UserCreationForm()
    
    return render(request, 'relationship_app/register.html', {'form': form})


# Role-check helper functions
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# Role-based views (must be here for checker)
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')