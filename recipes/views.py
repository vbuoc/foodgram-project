from django.shortcuts import render
from django.views.generic import ListView

from recipes.models import Recipe, Tag


class RecipeBaseView(ListView):
    # page_title = None
    paginate_by = 6
    queryset = Recipe.objects.all()


class IndexView(RecipeBaseView):
    template_name = 'recipes/index.html'
    extra_context = {'title': 'Рецепты'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

    def get_queryset(self):
        tags = self.request.GET.getlist('tag')
        return Recipe.objects.filter(tags__title__in=tags)


class RecipeViewSlug(ListView):
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