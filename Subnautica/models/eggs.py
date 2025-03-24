class Eggs:
    def __init__(self, egg, description, attitude, location):
        self.egg = egg
        self.description = description
        self.attitude = attitude
        self.location = location

    def get_img_name(self):
        return self.egg.lower().replace(" ", "_") + ".webp"

    def get_egg_url(self):
        return self.egg.lower().replace(" ", "_")

    def get_img_path(self):
        return f"img/Eggs/{self.get_img_name()}"

ampeel_egg = Eggs(
    "Ampeel Egg",
    "Ampeels spawn form this egg.",
    "Aggressive",
    [
        {"name" : "Blood Kelp Zone", "url" : "/subnautica/biomes/blood_kelp_zone/"},
        {"name" : "Bulb Zone", "url" : "/subnautica/biomes/bulb_zone/"}
    ]
)

eggs_list = [
    ampeel_egg,
]