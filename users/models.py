from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Модель пользователя, наследующая все поля встроенной модели
    """
    def __str__(self) -> str:
        return self.username
