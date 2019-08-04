from django.db import models

from core.models import User


class TeamMember(User):
    class Role(object):
        ADMIN = 'A'
        REGULAR = 'R'
        CHOICES = (
            (ADMIN, 'Admin'),
            (REGULAR, 'Regular')
        )
    role = models.CharField(max_length=3, choices=Role.CHOICES, default=Role.REGULAR)
