from django import template
from django.contrib.auth import get_user_model

from api.models import Favorite


register = template.Library()
User = get_user_model()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter
def declenize(number, args):
    args = [arg.strip() for arg in args.split(',')]
    last_digit = int(number) % 10
    if last_digit == 1:
        return f'{number} {args[0]}'
    elif 1 < last_digit < 5:
        return f'{number} {args[1]}'
    elif last_digit > 4 or last_digit == 0:
        return f'{number} {args[2]}'


@register.filter
def get_full_name_or_username(user):
    return user.get_full_name() or user.username


@register.filter
def is_favored(recipe, user):
    return Favorite.objects.filter(recipe=recipe, user=user).exists()


@register.filter
def is_in_shop_list_of(recipe, user):
    return False
    #return Purchase.objects.filter(recipe=recipe, user=user).exists()