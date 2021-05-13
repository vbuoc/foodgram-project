from django.shortcuts import render
from django.views.generic import ListView

from recipes.models import Recipe


class RecipeBaseView(ListView):
    queryset = Recipe.objects.all()


class IndexView(RecipeBaseView):
    pass