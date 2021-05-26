import io

from django.shortcuts import render
from django.http import FileResponse
from django.db.models import Sum

from purchases.purchase import Purchase
from purchases.utils import generate_pdf
from recipes.models import Recipe


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


def purchases_download(request):
    purchases = Purchase(request)
    recipe_ids = purchases.purchase.keys()
    ingredients = Recipe.objects.filter(
        id__in=recipe_ids
    ).prefetch_related(
        'ingredients'
    ).order_by(
        'ingredients__title'
    ).values(
        'ingredients__title', 'ingredients__dimension'
    ).annotate(amount=Sum('ingredients_amounts__quantity')).all()

    pdf = generate_pdf(
        'purchases/shopList_download.html', {'ingredients': ingredients}
    )

    return FileResponse(
        io.BytesIO(pdf),
        filename='ingredients.pdf',
        as_attachment=True
    )
