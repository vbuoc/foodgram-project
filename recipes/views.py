from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from api.models import Favorite
from recipes.forms import RecipeForm
from recipes.models import Recipe, Tag
from recipes.utils import recipe_save


class RecipeBaseView(ListView):
    paginate_by = 6

    def get_queryset(self):
        tags = self.request.GET.getlist(
            'tag',
            ['breakfast', 'lunch', 'dinner']
        )

        return Recipe.objects.filter(
            tags__title__in=tags
        ).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_tags'] = Tag.objects.all()
        return context


class IndexView(RecipeBaseView):
    template_name = 'recipes/index.html'
    extra_context = {'title': 'Рецепты'}


class RecipeViewDetail(DetailView):
    model = Recipe
    pk_url_kwarg = 'recipe_id'
    template_name = 'recipes/singlePage.html'
    context_object_name = 'recipe'


class RecipeNew(LoginRequiredMixin, CreateView):
    model = Recipe
    extra_context = {'title': 'Создание рецепта'}
    form_class = RecipeForm
    template_name = 'recipes/formRecipe.html'

    def form_valid(self, form):
        valid_form = recipe_save(self, form)
        return super().form_valid(valid_form)


class RecipeViewEdit(LoginRequiredMixin,
                     UserPassesTestMixin,
                     UpdateView):
    model = Recipe
    pk_url_kwarg = 'recipe_id'
    form_class = RecipeForm
    template_name = 'recipes/formRecipe.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class RecipeViewDelete(LoginRequiredMixin,
                       UserPassesTestMixin,
                       DeleteView):
    model = Recipe
    pk_url_kwarg = 'recipe_id'
    success_url = reverse_lazy('index')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def get(self, request, *args, **kwargs):
        """
        Using 'DeleteView' without Confirmation
        """
        return self.post(request, *args, **kwargs)


class Favorites(ListView):
    paginate_by = 6
    model = Favorite
    template_name = 'recipes/index.html'
    extra_context = {'title': 'Избранное'}

    def get_queryset(self):
        tags = self.request.GET.getlist(
            'tag',
            ['breakfast', 'lunch', 'dinner']
        )

        recipes = Recipe.objects.filter(
            favored_by__user=self.request.user,
            tags__title__in=tags
        ).select_related(
            'author'
        ).prefetch_related(
            'tags'
        ).distinct()

        return recipes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_tags'] = Tag.objects.all()
        return context


class ProfileView(RecipeBaseView):
    model = Recipe


class Subscriptions(ListView):
    pass


class PurchasesView(ListView):
    pass


class PurchasesDownloadView(ListView):
    pass
