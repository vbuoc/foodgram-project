import json

from django.shortcuts import render, redirect

from purchases.purchase import Purchase
from purchases.utils import get_pdf_file
from purchases.tasks import send_email_recipe_list


def purchases_view(request):
    template_name = 'purchases/shopList.html'
    purchases = Purchase(request)
    return render(
        request,
        template_name,
        {
            'title': 'Список покупок',
            'purchases': purchases
        }
    )


def purchases_download(request):
    purchases = Purchase(request)
    recipe_ids = purchases.purchase.keys()
    return get_pdf_file(recipe_ids)


def purchases_send_email(request):
    purchases = Purchase(request)
    recipe_ids_json = json.dumps(list(purchases.purchase.keys()))
    send_email_recipe_list.delay(
        request.user.id,
        recipe_ids_json
    )
    # send_email_recipe_list(
    #     request.user.id,
    #     recipe_ids_json
    # )
    return redirect('purchases')
