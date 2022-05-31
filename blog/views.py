from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from blog.models import Post
from blog.serializers import PostSerializer
from blog.permissions import IsAuthorOrReadOnly
from blog.services import get_all_posts, add_like, remove_like


class PostList(ListCreateAPIView):
    """
    View отображения полного списка постов
    """
    queryset = get_all_posts()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(RetrieveUpdateDestroyAPIView):
    """
    View отображения отдельного поста
    Для аутентифицированного пользователя есть доступ
    к редактированию своих постов
    """
    queryset = get_all_posts()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]


class PostLike(RetrieveAPIView):
    """
    View обработки лайков
    """
    queryset = get_all_posts()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.path.endswith('unlike'):
                remove_like(
                    self.request.user,
                    self.get_object()
                )
            else:
                add_like(
                    self.request.user,
                    self.get_object()
                )
            return self.retrieve(request, *args, **kwargs)
        return super().get(request)
