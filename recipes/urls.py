from django.urls import path, include

import recipes.views as recipes_views

recipes_urls = [
    path('new/', recipes_views.RecipeViewNew.as_view(), name='recipe_new'),
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
    path(
        'subscriptions/',
        recipes_views.Subscriptions.as_view(), name='subscriptions'
    ),
    path(
        '<str:username>/',
        recipes_views.ProfileView.as_view(), name='profile_view'
    ),
]
