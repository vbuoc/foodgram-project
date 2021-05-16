from django.urls import path, include

import recipes.views as recipes_views

recipes_urls = [
    path('new/', recipes_views.RecipeView.as_view(), name='recipe_new'),
    path(
        '<int:recipe_id>/<slug:slug>/',
        recipes_views.RecipeViewSlug,
        name='recipe_view_slug',
    ),
]

purchases_urls = [
    path('', recipes_views.PurchasesView.as_view(), name='purchases'),
    path('download/', recipes_views.PurchasesView.as_view(), name='purchases_download'),
]

urlpatterns = [
    path('', recipes_views.IndexView.as_view(), name='index'),
    path('subscriptions/', recipes_views.Subscriptions.as_view(), name='subscriptions'),
    path('favorites/', recipes_views.Favorites.as_view(), name='favorites'),
    path('<str:username>/', recipes_views.ProfileView.as_view(), name='profile_view'),
    path('purchases/', include(purchases_urls)),
    path('recipe/', include(recipes_urls)),
]