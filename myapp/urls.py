from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ItemViewSet

router = DefaultRouter()
router.register(r'products', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
