from rest_framework import mixins, filters, viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from api.serializers import (
    IngredientSerializer,
    FavoriteSerializer,
    SubscriptionSerializer,
    )
from api.models import Favorite, Subscription
from recipes.models import Ingredient, Recipe

from purchases.purchase import Purchase

User = get_user_model()


class CDViewSet(mixins.CreateModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet):

    def get_object(self, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {
            self.lookup_field: self.kwargs[lookup_url_kwarg],
            **kwargs,
        }

        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)

        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object(user=self.request.user)
        success = instance.delete()
        return Response({'success': bool(success)}, status=status.HTTP_200_OK)


class IngredientViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title', ]


class FavoriteViewSet(CDViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    lookup_field = 'recipe'


class SubscriptionViewSet(CDViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    lookup_field = 'author'


@api_view(['POST'])
def purchase_add(request):
    purchase = Purchase(request)
    recipe = get_object_or_404(Recipe, id=request.data.get('recipe'))
    if recipe:
        purchase.add(
            recipe=recipe,
            update_quantity=True
        )
        return Response({'success': True}, status=status.HTTP_200_OK)
    return Response({'success': False}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def purchase_delete(request, recipe_id):
    purchase = Purchase(request)
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe:
        purchase.remove(recipe)
        return Response({'success': True}, status=status.HTTP_200_OK)
    return Response({'success': False}, status=status.HTTP_404_NOT_FOUND)
