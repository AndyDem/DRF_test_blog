from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
    path('', views.PostList.as_view(), name='posts'),
    path('<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/like', views.PostLike.as_view(), name='post_like'),
    path('<int:pk>/unlike', views.PostLike.as_view(), name='post_unlike')
]

urlpatterns = format_suffix_patterns(urlpatterns)
