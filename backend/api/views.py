from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, CarSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Car

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer