from django.urls import path
from . import views
from .views import UserLoginView, UserRegisterView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('users/', views.CustomUserList.as_view()),
    path('users/<int:pk>/', views.CustomUserDetail.as_view()),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]