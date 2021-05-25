from django.shortcuts import render, redirect, get_object_or_404

from purchases.purchase import Purchase


def purchases_view(request):
    template_name = 'purchases/ShopList.html'
    purchases = Purchase(request)
    return render(
        request,
        template_name,
        {
            'title': 'Список покупок',
            'purchases': purchases
        }
    )