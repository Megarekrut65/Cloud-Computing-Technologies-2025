from django.urls import path
from .views import PaymentCreateView

urlpatterns = [
    path('process/', PaymentCreateView.as_view(), name='payment-create'),
]
