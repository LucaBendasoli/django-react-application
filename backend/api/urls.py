from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CarViewSet

router = DefaultRouter()
router.register(r'car', CarViewSet)

urlpatterns = [
    path('', include(router.urls))
]
