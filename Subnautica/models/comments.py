from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

User = get_user_model()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    parent = models.ForeignKey('self', null=True, blank=True, related_name="children", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['created_at']

    def get_view_url_name(self):
        model_name = self.content_type.model
        print("MODEL NAME", model_name)

        if model_name == "biomes":
            return "Subnautica:biome_view"
        elif model_name == "faunas":
            return "Subnautica:fauna_view"
        elif model_name == "floras":
            return "Subnautica:flora_view"
        elif model_name == "tools":
            return "Subnautica:tool_view"
        elif model_name == "vehicles":
            return "Subnautica:vehicle_view"
        elif model_name == "resources":
            return "Subnautica:resource_view"
        else:
            return ""

    def get_view_url_param(self):
        model_name = self.content_type.model
        print("MODEL NAME", model_name)

        if model_name == "biomes":
            return "biome_name"
        elif model_name == "faunas":
            return "fauna_name"
        elif model_name == "floras":
            return "flora_name"
        elif model_name == "tools":
            return "tool_name"
        elif model_name == "vehicles":
            return "vehicle_name"
        elif model_name == "resources":
            return "resource_name"
        else:
            return ""