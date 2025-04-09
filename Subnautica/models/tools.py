from django.db import models

class Tools(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    short_description = models.CharField(max_length=300)
    tool_type = models.CharField(max_length=100)
    build_time = models.IntegerField()
    attribute = models.CharField(max_length=100)

    def get_img_name(self):
        return self.name.lower().replace(" ", "_") + ".webp"

    def get_img_path(self):
        return f"img/Tools/{self.get_img_name()}"