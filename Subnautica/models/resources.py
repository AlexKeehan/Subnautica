from django.db import models

class Resources(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    obtain_from = models.CharField(max_length=100)
    biomes = models.ManyToManyField('Biomes', related_name='resources_biomes')
    size = models.IntegerField(default=0)

    def get_img_name(self):
        return self.name.lower().replace(" ", "_") + ".webp"

    def get_resource_url(self):
        return self.name.lower().replace(" ", "_")

    def get_img_path(self):
        return f"img/Resources/{self.get_img_name()}"