import requests
from django.conf import settings
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from .serializers import PaymentSerializer

ORDER_SERVICE_URL = "http://127.0.0.1:8002"

class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]  # 🔒 Тільки авторизовані користувачі

    def perform_create(self, serializer):
        order_id = self.request.data.get('order_id')
        headers = {"Authorization": self.request.headers.get("Authorization")}

        response = requests.get(f"{ORDER_SERVICE_URL}/orders/{order_id}/", headers=headers)
        if response.status_code == 200:
            serializer.save(status="paid")
        else:
            raise ValueError("Замовлення не знайдено")
