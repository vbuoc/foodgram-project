from django.urls import path
from purchases.views import purchases_view


urlpatterns = [
    path('purchases/', purchases_view, name='purchases'),
    # path('download/', views.purchases_download, name='purchases_download'),
]