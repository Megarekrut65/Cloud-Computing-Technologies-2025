import httpx
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['POST'])
def proxy_user_register(request):
    url = f"{settings.MICROSERVICE_URLS['user']}/api/v1/users/register/"
    response = httpx.post(url, json=request.data)
    return JsonResponse(response.json(), status=response.status_code)

@api_view(['POST'])
def proxy_user_login(request):
    url = f"{settings.MICROSERVICE_URLS['user']}/api/v1/users/login/"
    response = httpx.post(url, json=request.data)
    return JsonResponse(response.json(), status=response.status_code)

@api_view(['POST'])
def proxy_create_order(request):
    url = f"{settings.MICROSERVICE_URLS['order']}/api/v1/orders/create/"
    headers = {'Authorization': request.headers.get('Authorization', '')}
    response = httpx.post(url, json=request.data, headers=headers)
    return JsonResponse(response.json(), status=response.status_code)

@api_view(['POST'])
def proxy_payment(request):
    url = f"{settings.MICROSERVICE_URLS['payment']}/api/v1/payments/process/"
    headers = {'Authorization': request.headers.get('Authorization', '')}
    response = httpx.post(url, json=request.data, headers=headers)
    return JsonResponse(response.json(), status=response.status_code)
