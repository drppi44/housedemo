from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'main.views.home', name='home'),
    url(r'^flat/', include('main.urls')),

    url(r'^admin/', include(admin.site.urls)),
]