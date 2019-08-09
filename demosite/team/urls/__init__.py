from django.conf.urls import url, include


urlpatterns = [
    url('^v1/', include('team.urls.apiurls')),
]
