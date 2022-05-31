from typing import Any
from blog.models import Post
from django.db.models.query import QuerySet


def get_all_posts() -> QuerySet[Post]:
    return Post.objects.all()

def add_like(user: Any, post: Post) -> None:
    post.likes.add(user)
    post.save()


def remove_like(user: Any, post: Post) -> None:
    post.likes.add(user)
    post.save()
