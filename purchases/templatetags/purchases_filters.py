from django import template
from django.contrib.auth import get_user_model

from purchases.purchase import Purchase

register = template.Library()


@register.filter
def is_in_shop_list_of(request, recipe):
    purchase = Purchase(request)
    return purchase.find(recipe)