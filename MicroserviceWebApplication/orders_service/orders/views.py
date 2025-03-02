import requests
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Order
from .serializers import OrderSerializer

USER_SERVICE_URL = "http://127.0.0.1:8001"

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # 🔒 Тільки авторизовані користувачі

    def perform_create(self, serializer):
        user_id = self.request.user.id
        headers = {"Authorization": self.request.headers.get("Authorization")}

        response = requests.get(f"{USER_SERVICE_URL}/users/{user_id}/", headers=headers)
        if response.status_code == 200:
            serializer.save(user_id=user_id)
        else:
            raise ValueError("Користувач не знайдений")
