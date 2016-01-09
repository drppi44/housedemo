from django.conf.urls import url
from views import flat_add, house_add, filter_flat

urlpatterns = [
    url('^flat-add/$', flat_add, name='flat_add'),
    url('^house-add/$', house_add, name='house_add'),
    url('^filter/$', filter_flat, name='filter_flatt')
]
