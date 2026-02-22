from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

from notifications.models import Notification


CustomUser = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    filter_backends = [SearchFilter]
    search_fields = ["title", "content"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Feed view (posts from followed users)
@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def feed(request):

    following_users = request.user.following.all()

    posts = Post.objects.filter(author__in=following_users).order_by("-created_at")

    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


# Like a post
@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):

    post = get_object_or_404(Post, pk=pk)

    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        return Response({"message": "Already liked"}, status=400)

    Notification.objects.create(
        recipient=post.author,
        actor=request.user,
        verb="liked your post",
        content_type=ContentType.objects.get_for_model(post),
        object_id=post.id
    )

    return Response({"message": "Post liked"})


# Unlike a post
@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):

    post = get_object_or_404(Post, pk=pk)

    like = Like.objects.filter(user=request.user, post=post).first()

    if not like:
        return Response({"message": "You have not liked this post"}, status=400)

    like.delete()

    return Response({"message": "Post unliked"})