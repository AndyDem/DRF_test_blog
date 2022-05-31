from rest_framework import serializers
from django.contrib.auth import get_user_model


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Сериализатор для регистрации
    Использование функции get_user_model дает возможность использовать
    любую модель пользователя, зарегистрированную в проекте
    """
    password2 = serializers.CharField(
        style={'input_type': 'password'},
        label='Password confirmation',
        write_only=True
    )

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'password2'
        )
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            },
        }

    def save(self, **kwargs):
        user = get_user_model()(username=self.validated_data['username'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'}
            )
        user.set_password(password)
        user.save()
        return user
