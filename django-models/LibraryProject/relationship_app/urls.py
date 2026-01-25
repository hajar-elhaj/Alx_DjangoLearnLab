from django.urls import path 
from . import views
from django.views.generic import RedirectView
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    path('book/' , list_books, name = 'book_list'),
    path('library/<int:pk>/' , LibraryDetailView.as_view() , name = 'library_detail'),

        # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', RedirectView.as_view(url='/book/')),  # redirect root to /book/
]