from django.urls import path, include

import recipes.views as recipes_views

purchases_urls = [
    path('', recipes_views.PurchasesView.as_view(), name='purchases'),
    path('download/', recipes_views.PurchasesView.as_view(), name='purchases_download'),
]

recipes_urls = [
    path('new/', recipes_views.RecipeNew.as_view(), name='recipe_new'),
    path(
        '<int:recipe_id>/edit/',
        recipes_views.RecipeViewEdit.as_view(),
        name='recipe_edit',
    ),
    path(
        '<int:recipe_id>/delete/',
        recipes_views.RecipeViewDelete.as_view(),
        name='recipe_delete',
    ),
    path('<int:recipe_id>/',
         recipes_views.RecipeViewDetail.as_view(),
         name='recipe_detail',
         )
]

urlpatterns = [
    path('', recipes_views.IndexView.as_view(), name='index'),
    path('recipes/', include(recipes_urls)),
    path('favorites/', recipes_views.Favorites.as_view(), name='favorites'),
    path('subscriptions/', recipes_views.Subscriptions.as_view(), name='subscriptions'),
    path('purchases/', include(purchases_urls)),
    path('<str:username>/', recipes_views.ProfileView.as_view(), name='profile_view'),

]
