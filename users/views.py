from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from users.serializers import RegistrationSerializer


class Registartion(CreateAPIView):
    """
    View регистрации нового пользователя
    Использование функции get_user_model дает возможность использовать
    любую модель пользователя, зарегистрированную в проекте
    """
    model = get_user_model()
    serializer_class = RegistrationSerializer
