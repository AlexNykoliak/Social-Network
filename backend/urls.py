from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    #path('signup/'),
    #path('login/'),
    #path('post_create/'),
    path('posts/', views.PostList.as_view()),  # create post
    path('posts/<int:pk>/', views.PostDetail.as_view()),    # post detail by pk
    path('posts/<int:post_pk>/<int:user_pk>/like/', views.PostLikeView.as_view()),  # post like by user pk
    path('posts/<int:post_pk>/<int:user_pk>/unlike/', views.PostUnlikeView.as_view()),   # post unlike by user pk
    #path('analitics/date_from=<date_from>&date_to=<date_to>/'),
]
urlpatterns = format_suffix_patterns(urlpatterns)