"""
Permissions & Groups Setup:

Custom permissions are defined on the Book model:
- can_view
- can_create
- can_edit
- can_delete

Groups:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

Views are protected using @permission_required decorator.
"""

from django.shortcuts import render , redirect , get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from .forms import BookForm

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


# Role-based views 
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


#View a book
@permission_required('relationship_app.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/view_books.html', {'books': books})


#Create a book
@permission_required('relationship_app.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        year = request.POST.get('publication_year')

        Book.objects.create(
            title=title,
            author=author,
            publication_year=year
        )

    return render(request, 'relationship_app/create_book.html')



# Edit an existing book
@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()

    return render(request, 'relationship_app/edit_book.html', {'book': book})


# Delete a book
@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'POST':
        book.delete()

    return render(request, 'relationship_app/delete_book.html', {'book': book})