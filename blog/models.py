from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    """
    Модель поста в соцсети
    Использование функции get_user_model дает возможность использовать
    любую модель пользователя, зарегистрированную в проекте
    """
    title = models.CharField(max_length=150, blank=True, default='')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        related_name='posts',
        on_delete=models.CASCADE
    )
    likes = models.ManyToManyField(get_user_model(), related_name='likes')
