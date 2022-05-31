from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Permission, определяющий возможность редактирования постов
    только для их авторов
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
