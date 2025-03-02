import decouple
import requests
from rest_framework import generics

from .models import Order
from .serializers import OrderSerializer

USER_SERVICE_URL = decouple.config('USER_SERVICE_URL')

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes= []

    def perform_create(self, serializer):
        headers = {"Authorization": self.request.headers.get("Authorization")}

        response = requests.get(f"{USER_SERVICE_URL}/user/", headers=headers)
        if response.status_code == 200:
            serializer.save(user_id=response.json().get("id"))
        else:
            raise ValueError("User not found!")

class OrderRetrieveView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = []
