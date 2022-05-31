from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
    path('register', views.Registartion.as_view(), name='registration'),
    path('', include('rest_framework.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
