from django.urls import path
from purchases.views import purchases_view, purchases_download


urlpatterns = [
    path('purchases/', purchases_view, name='purchases'),
    path('purchases/download/', purchases_download, name='purchases_download'),
]