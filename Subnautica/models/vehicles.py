from django.db import models

class Vehicles(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    short_description = models.CharField(max_length=300)
    velocity = models.CharField(max_length=300)
    health = models.IntegerField()
    acq_from = models.CharField(max_length=100)

    def get_img_name(self):
        return self.name.lower().replace(" ", "_") + ".webp"

    def get_img_path(self):
        return f"img/Vehicles/{self.get_img_name()}"

    @classmethod
    def get_view_url_name(cls):
        return 'Subnautica:vehicle_view'

    @classmethod
    def get_view_url_param(cls):
        return 'vehicle_name'