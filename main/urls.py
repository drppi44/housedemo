from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$', views.flat, name='flat'),
    url('^flat-add/$', views.flat_add, name='flat_add'),
    url('^house-add/$', views.house_add, name='house_add')
]
