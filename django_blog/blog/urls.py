from django.urls import path
from .views import (
    register_view, login_view, logout_view, profile_view,
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

urlpatterns = [
    # Authentication
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),

    # Blog CRUD
    path('', ListView.as_view(), name='post-list'),
    path('posts/new/', CreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', DetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', UpdateView.as_view(), name='post-edit'),
    path('posts/<int:pk>/delete/', DeleteView.as_view(), name='post-delete'),
]