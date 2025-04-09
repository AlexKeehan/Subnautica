from django.db import models

class Faunas(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    fauna_type = models.CharField(max_length=100)
    attitude = models.CharField(max_length=50)
    biomes = models.ManyToManyField("Biomes", "faunas_biomes")

    def get_img_name(self):
        return self.name.lower().replace(" ", "_") + ".webp"

    def get_img_path(self):
        return f"img/Fauna/{self.get_img_name()}"