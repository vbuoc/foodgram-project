from django.contrib import admin
from django.db.models import Count

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from recipes.models import (
    Ingredient,
    Recipe,
    RecipeIngredient,
    Tag
)


class IngredientResource(resources.ModelResource):
    class Meta:
        model = Ingredient
        fields = ('title', 'dimension')


@admin.register(Ingredient)
class IngredientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'dimension')
    search_fields = ('^title', )
    resource_class = IngredientResource


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    min_num = 1
    extra = 0
    verbose_name = 'ингредиент'


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientInline, )
    list_display = (
        'id', 'title', 'author', 'slug',
        'cooking_time', 'get_favorites_count', 'pub_date'
    )
    list_filter = ('author', 'tags__title')
    search_fields = ('title', 'author__username')
    autocomplete_fields = ('author', )
    ordering = ('-pub_date', )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(favorite_count=Count('favored_by'))

    @staticmethod
    def get_favorites_count(obj):
        return obj.favorite_count


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'color', 'display_name')
    list_filter = ('display_name',)
