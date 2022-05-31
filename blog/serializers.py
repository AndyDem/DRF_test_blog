from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Сериализатор постов соцсети
    """
    author = serializers.ReadOnlyField(source='author.username')
    likes = serializers.ReadOnlyField(source='likes.count')

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'created_at', 'author', 'likes']
