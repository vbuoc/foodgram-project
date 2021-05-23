from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    IngredientViewSet,
    FavoriteViewSet,
    SubscriptionViewSet
)

router = DefaultRouter()

router.register('favorites', FavoriteViewSet, basename='favorites')
router.register(r'ingredients', IngredientViewSet, basename='ingredients')
router.register(
    r'subscriptions',
    SubscriptionViewSet,
    basename='subscriptions',
)

urlpatterns = [
    path('v1/', include(router.urls)),
]