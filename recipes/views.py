from django.shortcuts import render
from django.views.generic import ListView

from recipes.models import Recipe


class RecipeBaseView(ListView):
    page_title = None
    queryset = Recipe.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self._get_title
        return context

    def _get_title(self):
        return self.page_title


class IndexView(RecipeBaseView):
    template_name = 'recipes/index.html'
    page_title = 'Рецепты'
    pass


class Subscriptions(ListView):
    pass


class Favorites(ListView):
    pass


class ProfileView(ListView):
    pass


class RecipeView(ListView):
    pass


class PurchasesView(ListView):
    pass


class PurchasesDownloadView(ListView):
    pass