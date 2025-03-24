class Faunas:
    def __init__(self, fauna, description, attitude, biome):
        self.fauna = fauna
        self.description = description
        self.attitude = attitude
        self.biome = biome

    def get_img_name(self):
        return self.fauna.lower().replace(" ", "_") + ".webp"

    def get_fauna_url(self):
        return self.fauna.lower().replace(" ", "_")

    def get_img_path(self):
        return f"img/Fauna/{self.get_img_name()}"

amoeboid = Faunas(
    "Amoeboid",
    "",
    "Passive",
    [
        {"name" : "Lost River", "url" : "/subnautica/biomes/lost_river/"}
    ]
)

faunas_list = [
    amoeboid,
]