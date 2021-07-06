import pdfkit
import io

from django.template.loader import get_template
from django.http import FileResponse
from django.db.models import Sum

from recipes.models import Recipe


def generate_pdf(template_name, context):
    pdf_options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None
    }
    html = get_template(template_name).render(context)
    return pdfkit.from_string(html, False, options=pdf_options)


def get_pdf_file(recipe_ids):
    pdf = get_pdf_data(recipe_ids)

    return FileResponse(
        io.BytesIO(pdf),
        filename='ingredients.pdf',
        as_attachment=True
    )


def get_pdf_data(recipe_ids):
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

    return pdf
