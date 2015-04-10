from django.conf.urls import patterns, url
from rest_framework.authtoken.views import ObtainAuthToken
from accounts.views import RegisterUserView, UserDetailsView


urlpatterns = patterns('',
    url(r'^register/$', RegisterUserView.as_view(), name='register'),
    url(r'^login/$', ObtainAuthToken.as_view(), name='login'),
    url(r'^details/$', UserDetailsView.as_view(), name='login'),
)
