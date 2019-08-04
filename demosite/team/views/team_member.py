from rest_framework.viewsets import ModelViewSet

from team.models import TeamMember
from team.serializers import TeamMemberSerializer


class TeamMemberViewSet(ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

