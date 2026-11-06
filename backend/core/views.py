from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def item_list(request):
    items = [
        {"id": 1, "name": "Eggs", "is_purchased": False},
        {"id": 2, "name": "Milk", "is_purchased": False},
        {"id": 3, "name": "Bread", "is_purchased": True},
    ]
    return Response(items)