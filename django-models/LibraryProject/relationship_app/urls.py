from django.urls import path 
from .views import RegisterView, CustomLoginView, CustomLogoutView
from django.views.generic import RedirectView
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    path('book/' , list_books, name = 'book_list'),
    path('library/<int:pk>/' , LibraryDetailView.as_view() , name = 'library_detail'),

        # Authentication URLs
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('', RedirectView.as_view(url='/book/')),  # redirect root to /book/
]