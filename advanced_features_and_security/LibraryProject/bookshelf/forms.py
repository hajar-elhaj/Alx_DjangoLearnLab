from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    """
    ExampleForm for demonstrating CSRF protection and safe form handling.
    Uses the Book model.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
