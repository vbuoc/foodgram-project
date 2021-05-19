from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from recipes.models import Recipe, Tag
from recipes.forms import RecipeForm
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
    success_url = reverse_lazy('recipe_detail')

    # permission_required = ('news.add_post')

    def form_valid(self, form):
        valid_form = recipe_save(self, form)
        return super().form_valid(valid_form)


class RecipeViewEdit(RecipeBaseView):
    pass


class ProfileView(RecipeBaseView):
    model = Recipe


class Subscriptions(ListView):
    pass


class Favorites(ListView):
    pass


class PurchasesView(ListView):
    pass


class PurchasesDownloadView(ListView):
    pass
