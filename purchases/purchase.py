from decimal import Decimal
from django.conf import settings

from recipes.models import Recipe


class Purchase(object):
    purchase = None

    def __init__(self, request):
        self.session = request.session
        purchase = self.session.get(settings.PURCHASE_SESSION_ID)
        if not purchase:
            purchase = self.session[settings.PURCHASE_SESSION_ID] = {}
        self.purchase = purchase

    def find(self, recipe):
        recipe_id = str(recipe.id)
        return recipe_id in self.purchase

    def add(self, recipe, quantity=1, update_quantity=False):
        recipe_id = str(recipe.id)
        if recipe_id not in self.purchase:
            self.purchase[recipe_id] = {'quantity': 0}
        if update_quantity:
            self.purchase[recipe_id]['quantity'] = quantity
        else:
            self.purchase[recipe_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.PURCHASE_SESSION_ID] = self.purchase
        self.session.modified = True

    def remove(self, recipe):
        recipe_id = str(recipe.id)
        if recipe_id in self.purchase:
            del self.purchase[recipe_id]
            self.save()

    def clear(self):
        del self.session[settings.PURCHASE_SESSION_ID]
        self.session.modified = True

    def __iter__(self):
        recipe_ids = self.purchase.keys()
        recipes = Recipe.objects.filter(id__in=recipe_ids)

        for recipe in recipes:
            self.purchase[str(recipe.id)]['recipe'] = recipe

        for item in self.purchase.values():
            item['total_quantity'] = item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.purchase.values())