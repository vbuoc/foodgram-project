import json

from celery import shared_task

from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model

from purchases.utils import get_pdf_data

User = get_user_model()


@shared_task
def send_email_recipe_list(user_id, recipe_ids_json):
    user = User.objects.get(id=user_id)
    if not user.is_authenticated:
        raise ValueError("user is not authenticated")

    email_address = user.email
    if not email_address:
        raise ValueError('email is empty')

    print('[\/] begin email sending to', email_address)

    if isinstance(email_address, str):
        recipient_list = [email_address]
    else:
        recipient_list = email_address

    email = EmailMessage(
        subject=f'{user.first_name}. Your recipes list',
        body='Это письмо сгенерировано автоматически,\n'
             ' отвечать на него не нужно',
        to=recipient_list,
    )

    recipe_ids = json.loads(recipe_ids_json)
    if recipe_ids:
        pdf_data = get_pdf_data(recipe_ids=recipe_ids)
        email.attach('RecipeList.pdf', pdf_data)

    result = email.send(fail_silently=False)

    print(
        '[/\] end email sending',
        'True' if result > 0 else 'False'
    )

    return True if result > 0 else False
