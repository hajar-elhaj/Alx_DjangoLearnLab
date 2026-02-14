from django.urls import path
from .views import (
    register_view, login_view, logout_view, profile_view,
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .views import (
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)
from .views import SearchResultsView, ListView

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
    path('post/<int:pk>/update/', UpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', DeleteView.as_view(), name='post-delete'),

    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    path('search/', SearchResultsView.as_view(), name='search-results'),
    path('tags/<slug:tag_slug>/', PostsByTagView.as_view(), name='posts-by-tag'),
]