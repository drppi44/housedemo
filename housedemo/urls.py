from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', 'main.views.home', name='home'),
    url(r'^flat/', include('main.urls')),

    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)