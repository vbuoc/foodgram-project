from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    IngredientViewSet,
    FavoriteViewSet
)

router = DefaultRouter()

router.register('favorites', FavoriteViewSet, basename='favorites')
router.register(r'ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = [
    path('v1/', include(router.urls)),
]