from rest_framework.routers import DefaultRouter
from .views import FavoriteItemViewSet

router = DefaultRouter()
router.register(r'items', FavoriteItemViewSet, basename='favoriteitem')

urlpatterns = router.urls
