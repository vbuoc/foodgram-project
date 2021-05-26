from django import template

from purchases.purchase import Purchase

register = template.Library()


@register.filter
def is_in_shop_list_of(request, recipe):
    purchase = Purchase(request)
    return purchase.find(recipe)
