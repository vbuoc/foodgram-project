from django.contrib import admin
from django.contrib.flatpages.views import flatpage
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

flatpages_urls = [
    path('author/', flatpage, {'url': '/author/'}, name='about_author'),
    path('tech/', flatpage, {'url': '/tech/'}, name='about_tech'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('about/', include(flatpages_urls)),
    path('api/', include('api.urls')),
    path('', include('recipes.urls')),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
