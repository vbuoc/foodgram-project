from rest_framework import mixins, filters, viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from api.serializers import (
    IngredientSerializer,
    FavoriteSerializer
    )
from api.models import Favorite
from recipes.models import Ingredient

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
    serializer_class = IngredientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title', ]

    def get_queryset(self):
        data = self.request.GET['query']
        if data is not None:
            queryset = Ingredient.objects.filter(title__istartswith=data)
            return queryset
        return Ingredient.objects.none()


class FavoriteViewSet(CDViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    lookup_field = 'recipe'