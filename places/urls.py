from django.conf.urls import include, url
from places.views import *

urlpatterns = (
    url(
        r'^(?P<lat>-?[0-9]+\.?[0-9]*)/(?P<lon>-?[0-9]+\.?[0-9]*)/$',
        LocationList.as_view(),
        name='location_list'
    ),
)
