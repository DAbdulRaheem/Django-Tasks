from rest_framework import viewsets
from .models import FavoriteItem
from .serializers import FavoriteItemSerializer

class FavoriteItemViewSet(viewsets.ModelViewSet):
    queryset = FavoriteItem.objects.all().order_by('-created_at')
    serializer_class = FavoriteItemSerializer
