from decimal import Decimal

from django.db import transaction, IntegrityError
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404

from recipes.models import Ingredient, RecipeIngredient


def get_front_ingredients(request):
    ingredients = []
    for key, name in request.POST.items():
        if key.startswith('nameIngredient'):
            num = key.split('_')[1]
            dimension = request.POST[
                f'unitsIngredient_{num}'
            ]
            quantity = request.POST[
                f'valueIngredient_{num}'
            ]

            ingredients.append(
                {
                    'title': name,
                    'dimension': dimension,
                    'quantity': quantity
                }
            )

    return ingredients


def recipe_save(self, form):
    try:
        with transaction.atomic():

            recipe = form.save(commit=False)
            recipe.author = self.request.user
            recipe.save()

            objects = []
            ingredients = get_front_ingredients(self.request)
            for item in ingredients:
                ingredient = get_object_or_404(
                    Ingredient,
                    title=item['title'],
                    dimension=item['dimension']
                )
                quantity = item['quantity']

                objects.append(
                    RecipeIngredient(
                        recipe=recipe,
                        ingredient=ingredient,
                        quantity=Decimal(quantity.replace(',', '.'))
                    )
                )
            RecipeIngredient.objects.bulk_create(objects)
            form.save_m2m()
            return recipe

    except IntegrityError:
        raise HttpResponseBadRequest


def recipe_edit(self, form, instance):
    try:
        with transaction.atomic():
            RecipeIngredient.objects.filter(recipe=instance).delete()
            return recipe_save(self, form)
    except IntegrityError:
        raise HttpResponseBadRequest