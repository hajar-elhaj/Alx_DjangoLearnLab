from django.shortcuts import render , redirect
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login, logout, authenticate

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
# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/book/')  # redirect after login
    else:
        form = AuthenticationForm()
    
    return render(request, 'relationship_app/login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('/login/')  # redirect after logout          