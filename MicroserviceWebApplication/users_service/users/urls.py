from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserListView, RegisterView, LoginView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
