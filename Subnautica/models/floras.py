from django.db import models

class Floras(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    use = models.CharField(max_length=100)
    attitude = models.CharField(max_length=100)
    obtain_from = models.CharField(max_length=100)
    biomes = models.ManyToManyField("Biomes", "floras_biomes")
    growth_time = models.IntegerField()

    def get_img_name(self):
        return self.name.lower().replace(" ", "_") + ".webp"

    def get_flora_url(self):
        flora_url = self.name.lower().replace(" ", "_")
        print(f"Flora URL: {flora_url}")
        return flora_url

    def get_img_path(self):
        return f"img/Flora/{self.get_img_name()}"