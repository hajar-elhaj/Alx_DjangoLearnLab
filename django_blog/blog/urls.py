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
    path('post/new/', CreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', DetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/edit/', UpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/update/', UpdateView.as_view(), name='post-update')
    path('post/<int:pk>/delete/', DeleteView.as_view(), name='post-delete'),
]