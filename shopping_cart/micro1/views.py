from django.contrib.auth.models import Permission
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, renderers
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response

# Create your views here.
# ModelViewSet proporciona todos los metodos
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class PaymentDetailViewSet(viewsets.ModelViewSet):

    queryset = PaymentDetail.objects.all()
    serializer_class = PaymentDetailSerializer


class ShoppingCartViewSet(viewsets.ModelViewSet): 
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer


class CartDetailViewSet(viewsets.ModelViewSet):
    queryset = CartDetail.objects.all()
    serializer_class = CartDetailSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class SaleDetailViewSet(viewsets.ModelViewSet):
    queryset = SaleDetail.objects.all()
    serializer_class = SaleDetailSerializer