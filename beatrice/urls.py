from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = (
    url(r'^api/accounts/', include('accounts.urls')),
    url(r'^api/tasks/', include('tasks.urls')),
    url(r'^api/places/', include('places.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
