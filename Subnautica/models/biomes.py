from django.db import models

class Biomes(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    short_description = models.CharField(max_length=300)
    biome_type = models.CharField(max_length=50)
    depth_range = models.IntegerField(default=0)
    temp_range = models.CharField(max_length=100)
    resources = models.ManyToManyField('Resources', related_name='biomes_resources')

    def get_img_name(self):
        return self.name.lower().replace(" ", "_") + ".webp"

    def get_img_path(self):
        return f"img/Biomes/{self.get_img_name()}"