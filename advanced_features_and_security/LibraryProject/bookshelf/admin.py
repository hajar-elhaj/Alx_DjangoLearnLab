from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in the admin list view
    search_fields = ('title', 'author')  # Add search box for title & author
    list_filter = ('publication_year',)  # Add filter sidebar for publication year

# Register the Book model with the custom admin
admin.site.register(Book, BookAdmin)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Information', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

    list_display = ('username', 'email', 'is_staff', 'is_active')