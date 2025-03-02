from django.urls import path
from .views import OrderCreateView, OrderRetrieveView

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order-create'),
    path('get/<int:pk>', OrderRetrieveView.as_view(), name='order-get'),
]
