from django.conf.urls import url
from django.contrib import admin
from django.urls import include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('demosite.urls.apiurls')),

]

urlpatterns += staticfiles_urlpatterns()
