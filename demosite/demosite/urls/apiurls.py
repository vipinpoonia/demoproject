from django.conf.urls import url, include


urlpatterns = [
    url('^api/', include('team.urls')),
]
