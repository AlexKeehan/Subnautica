class Faunas:
    def __init__(self, fauna, description, fauna_type, attitude, biomes):
        self.fauna = fauna
        self.description = description
        self.fauna_type = fauna_type
        self.attitude = attitude
        self.biomes = biomes

    def get_img_name(self):
        return self.fauna.lower().replace(" ", "_") + ".webp"

    def get_fauna_url(self):
        return self.fauna.lower().replace(" ", "_")

    def get_img_path(self):
        return f"img/Fauna/{self.get_img_name()}"

amoeboid = Faunas(
    "Amoeboid",
    "The Amoeboid is a passive fauna species that can be found exclusively in the Lost River. It is found in abundance within this biome and can usually be spotted in large groups.",
    "Parasite",
    "Passive",
    [
        {"name" : "Lost River", "url" : "/subnautica/biomes/lost_river/"}
    ]
)

faunas_list = [
    amoeboid,
]