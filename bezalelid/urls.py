from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from decouple import config

urlpatterns = [
    path('', include('graduates.urls')),
    path('admin/', admin.site.urls),
]

if not config('DEPLOYED', cast=bool):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
