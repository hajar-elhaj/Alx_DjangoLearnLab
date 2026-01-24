from django.urls import path 
from . import views

urlpatterns = [
    path('book/' , views.book_list, name = 'book_list'),
    path('library/<int:pk>/' , views.LibraryDetailView.as_view() , name = 'library_detail')
]