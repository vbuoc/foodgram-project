from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    IngredientViewSet,
    FavoriteViewSet,
    SubscriptionViewSet,
    purchase_add,
    purchase_delete
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

# Purchases
purchases_urls = [
    path(r'purchases/', purchase_add, name='purchase_add'),
    path(r'purchases/<int:recipe_id>/', purchase_delete, name='purchase_delete'),
]

urlpatterns += [
    path('v1/', include(purchases_urls)),
]
