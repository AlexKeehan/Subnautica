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

    def get_img_path(self):
        return f"img/Flora/{self.get_img_name()}"

    @classmethod
    def get_view_url_name(cls):
        return 'Subnautica:flora_view'

    @classmethod
    def get_view_url_param(cls):
        return 'flora_name'