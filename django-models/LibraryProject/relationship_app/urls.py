from django.urls import path 
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import RedirectView
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    path('book/' , list_books, name = 'book_list'),
    path('library/<int:pk>/' , LibraryDetailView.as_view() , name = 'library_detail'),

        # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('', RedirectView.as_view(url='/book/')),  # redirect root to /book/
]