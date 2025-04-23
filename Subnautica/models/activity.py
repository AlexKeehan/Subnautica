from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Activity(models.Model):

    ACTIVITY_TYPES = [
        ("VISIT", "Page Visit"),
        ("COMMENT", "Comment Posted"),
        ("REPLY", "Reply Posted"),
        ("ROLE_UPDATED", "Role Updated"),
        ("UPDATED_ROLE", "Updated Role"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=100)
    action_time = models.DateTimeField(default=timezone.now)
    item_type = models.CharField(max_length=100)
    item_name = models.CharField(max_length=255)
    url = models.URLField()
    related_comment = models.ForeignKey('Comment', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} {self.action_type} on {self.item_name}'

    def get_activity_msg(self):
        if self.action_type == "VISIT":
            return f"You visited {self.item_name}"
        elif self.action_type == "COMMENT":
            return f"You commented on {self.item_name}"
        elif self.action_type == "REPLY":
            return f"Someone replied to you on {self.item_name}"
        elif self.action_type == "ROLE_UPDATED":
            return f"Your Permissions have changed"
        elif self.action_type == "UPDATED_ROLE":
            return f"You changed permissions for {self.item_name}"
        else:
            return ""