from django.urls import path
from purchases.views import (
    purchases_view,
    purchases_download,
    purchases_send_email,
)


urlpatterns = [
    path('purchases/', purchases_view, name='purchases'),
    path('purchases/download/', purchases_download, name='purchases_download'),
    path('purchases/send_email', purchases_send_email, name='purchases_send_email')
]
