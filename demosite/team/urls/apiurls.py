from django.urls import path, include
from rest_framework import routers

from team.views import TeamMemberViewSet

router = routers.DefaultRouter()

router.register(r'team-members', TeamMemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
