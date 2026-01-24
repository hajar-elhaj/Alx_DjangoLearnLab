from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in the admin list view
    search_fields = ('title', 'author')  # Add search box for title & author
    list_filter = ('publication_year',)  # Add filter sidebar for publication year

# Register the Book model with the custom admin
admin.site.register(Book, BookAdmin)
