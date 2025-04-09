from django.db import models

class Eggs(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    attitude = models.CharField(max_length=50)
    fauna = models.ForeignKey("Faunas", on_delete=models.CASCADE)
    biomes = models.ManyToManyField("Biomes", "eggs_biomes")

    def get_img_name(self):
        return self.name.lower().replace(" ", "_") + ".webp"

    def get_img_path(self):
        return f"img/Eggs/{self.get_img_name()}"

    def get_fauna_url(self):
        return self.fauna.name.lower().replace(" ", "_")