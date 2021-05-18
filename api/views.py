from rest_framework.mixins import ListModelMixin
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet

from api.serializers import IngredientSerializer

from recipes.models import Ingredient


class IngredientViewSet(ListModelMixin, GenericViewSet):
    # queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = [SearchFilter]
    search_fields = ['^title', ]

    def get_queryset(self):
        data = self.request.GET['query']
        if data is not None:
            queryset = Ingredient.objects.filter(title__istartswith=data)
            return queryset
        return Ingredient.objects.none()
