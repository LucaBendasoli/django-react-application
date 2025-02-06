from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, CarSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import Car

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()