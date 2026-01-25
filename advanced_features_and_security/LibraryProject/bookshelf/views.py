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

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book
from .forms import ExampleForm


#View a book
@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})


#Create a book
@permission_required('bookshelf.can_create', raise_exception=True)
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

    return render(request, 'bookshelf/create_book.html')



# Edit an existing book
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()

    return render(request, 'bookshelf/edit_book.html', {'book': book})


# Delete a book
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'POST':
        book.delete()

    return render(request, 'bookshelf/delete_book.html', {'book': book})

# List all books
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # or wherever you want
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})