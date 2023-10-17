from django.urls import path
from . import views
from .views import UserLoginView

urlpatterns = [
    path('users/', views.CustomUserList.as_view()),
    path('users/<int:pk>/', views.CustomUserDetail.as_view()),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
]