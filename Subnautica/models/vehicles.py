class Vehicles:
    def __init__(self, vehicle, description, short_description, velocity, health, aqq_from):
        self.vehicle = vehicle
        self.description = description
        self.short_description = short_description
        self.velocity = velocity
        self.health = health
        self.aqq_from = aqq_from

    def get_img_name(self):
        return self.vehicle.lower().replace(" ", "_") + ".webp"

    def get_vehicle_url(self):
        return self.vehicle.lower().replace(" ", "_")

    def get_img_path(self):
        return f"img/Vehicles/{self.get_img_name()}"

cyclops = Vehicles(
    "Cyclops",
    """
    The Cyclops is a vast multi-person submarine capable of functioning as a mobile base.
    It also features an onboard artificial intelligence, multiple upgrade systems, sonar, fire suppression systems, and camera systems.
    """,
    "A vast industrial-grade multiple person submarine",
    "Ahead Slow: 5.4"
    "Ahead Standard: 8.2"
    "Ahead Flank: 10.5"
    "Reverse:4.8"
    "Vertical: 3.1",
    1500,
    "Fragments"
)

vehicles_list = [
    cyclops,
]