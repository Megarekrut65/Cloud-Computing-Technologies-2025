import decouple
import requests
from django.conf import settings
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from .serializers import PaymentSerializer

ORDER_SERVICE_URL = decouple.config('ORDER_SERVICE_URL')

class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    authentication_classes= []

    def perform_create(self, serializer):
        order_id = self.request.data.get('order_id')
        headers = {"Authorization": self.request.headers.get("Authorization")}

        response = requests.get(f"{ORDER_SERVICE_URL}/get/{order_id}", headers=headers)
        if response.status_code == 200:
            serializer.save(status="paid")
        else:
            raise ValueError("Order not found!")
