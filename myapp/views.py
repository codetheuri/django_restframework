from rest_framework import viewsets
from .models import Item
from .serializers import Itemserializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = Itemserializer
