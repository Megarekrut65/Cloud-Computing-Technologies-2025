from django.urls import path
from .views import proxy_user_register, proxy_user_login, proxy_create_order, proxy_payment

urlpatterns = [
    path('register/', proxy_user_register, name='proxy_register'),
    path('login/', proxy_user_login, name='proxy_login'),
    path('orders/', proxy_create_order, name='proxy_create_order'),
    path('payment/', proxy_payment, name='proxy_payment'),
]
