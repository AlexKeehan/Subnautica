class Eggs:
    def __init__(self, egg, description, attitude, fauna, locations):
        self.egg = egg
        self.description = description
        self.attitude = attitude
        self.fauna = fauna
        self.locations = locations


    def get_img_name(self):
        return self.egg.lower().replace(" ", "_") + ".webp"

    def get_egg_url(self):
        return self.egg.lower().replace(" ", "_")

    def get_img_path(self):
        return f"img/Eggs/{self.get_img_name()}"

    def get_fauna_url(self):
        return self.fauna.lower().replace(" ", "_")

ampeel_egg = Eggs(
    "Ampeel Egg",
    "Ampeels spawn form this egg.",
    "Aggressive",
    "Ampeel",
    [
        {"name" : "Blood Kelp Zone", "url" : "/subnautica/biomes/blood_kelp_zone/"},
        {"name" : "Bulb Zone", "url" : "/subnautica/biomes/bulb_zone/"}
    ],

)

eggs_list = [
    ampeel_egg,
]