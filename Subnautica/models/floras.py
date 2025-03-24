class Floras:
    def __init__(self, flora, description, use, attitude, obtain_from, biome, growth_time):
        self.flora = flora
        self.description = description
        self.use = use
        self.attitude = attitude
        self.obtain_from = obtain_from
        self.biome = biome
        self.growth_time = growth_time

    def get_img_name(self):
        return self.flora.lower().replace(" ", "_") + ".webp"

    def get_flora_url(self):
        flora_url = self.flora.lower().replace(" ", "_")
        print(f"Flora URL: {flora_url}")
        return flora_url

    def get_img_path(self):
        return f"img/Flora/{self.get_img_name()}"

bloodroot = Floras(
    "Bloodroot",
    """
    Bloodroot is a flora species that are prominent in the Blood Kelp Caves.
    They appear as large root-like plants that protrude from the seabed.
    They are known for growing Blood Oil.
    """,
    "N/A",
    "Harvestable",
    "N/A",
    [
        {"name": "Blood Kelp Caves", "url": "/subnautica/biomes/blood_kelp_caves"},
        {"name": "Blood Kelp Zone", "url": "/subnautica/biomes/blood_kelp_zone"}
    ],
    "N/A"
)

floras_list = [
    bloodroot,
]