class Vehicles:
    def __init__(self, vehicle, description, short_description, velocity, health, acq_from):
        self.vehicle = vehicle
        self.description = description
        self.short_description = short_description
        self.velocity = velocity
        self.health = health
        self.acq_from = acq_from

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
    """
    <ul>
        <li><a>Ahead Slow: 5.4</a></li>
        <li><a>Ahead Standard: 8.2</a></li>
        <li><a>Flank: 10.5</a></li>
        <li><a>Reverse: 4.8</a></li>
        <li><a>Vertical: 3.1</a></li>
    </ul>

    """,
    1500,
    "Fragments"
)

vehicles_list = [
    cyclops,
]