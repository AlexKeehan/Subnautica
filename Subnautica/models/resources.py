class Resources:
    def __init__(self, resource, description, obtain_from, locations, size):
        self.resource = resource
        self.description = description
        self.obtain_from = obtain_from
        self.locations = locations
        self.size = size

    def get_img_name(self):
        return self.resource.lower().replace(" ", "_") + ".webp"

    def get_resource_url(self):
        return self.resource.lower().replace(" ", "_")

    def get_img_path(self):
        return f"img/Resources/{self.get_img_name()}"

titanium = Resources(
    "Titanium",
    """
    Titanium is a material that is heavily used in many crafting recipes.
    It is one of the earliest resources the player can obtain and is very common.
    """,
    """
    Large Resource Deposits <br/>
    Limestone Outcrop
    """,
    [
        {"name": "Bulb Zone", "url": "/subnautica/biomes/bulb_zone/"},
        {"name": "Crag Field", "url": "/subnautica/biomes/crag_field/"},
        {"name": "Crash Zone", "url": "/subnautica/biomes/crash_zone/"},
        {"name": "Crash Zone Mesas", "url": "/subnautica/biomes/crash_zone_mesas/"},
        {"name": "Deep Grand Reef", "url": "/subnautica/biomes/deep_grand_reef/"},
        {"name": "Dunes", "url": "/subnautica/biomes/dunes/"},
        {"name": "Dunes Caves", "url": "/subnautica/biomes/dunes_caves/"},
        {"name": "Grand Reef", "url": "/subnautica/biomes/grand_reef/"},
        {"name": "Grassy Plateaus", "url": "/subnautica/biomes/grassy_plateaus/"},
        {"name": "Grassy Plateaus Caves", "url": "/subnautica/biomes/grassy_plateaus_caves/"},
        {"name": "Kelp Forest", "url": "/subnautica/biomes/kelp_forest/"},
        {"name": "Kelp Forest Caves", "url": "/subnautica/biomes/kelp_forest_caves/"},
        {"name": "Inactive Lava Zone", "url": "/subnautica/biomes/inactive_lava_zone/"},
        {"name": "Inactive Lava Zone Corridor", "url": "/subnautica/biomes/inactive_lava_zone_corridor/"},
        {"name": "Lost River", "url": "/subnautica/biomes/lost_river/"},
        {"name": "Mushroom Forest", "url": "/subnautica/biomes/mushroom_forest/"},
        {"name": "Safe Shallows", "url": "/subnautica/biomes/safe_shallows/"},
        {"name": "Safe Shallows Caves", "url": "/subnautica/biomes/safe_shallows_caves/"},
        {"name": "Sea Treader's Path", "url": "/subnautica/biomes/sea_treaders_path/"},
        {"name": "Sea Treader's Tunnel Caves", "url": "/subnautica/biomes/sea_treaders_tunnel_caves/"},
        {"name": "Sparse Reef", "url": "/subnautica/biomes/sparse_reef/"},
        {"name": "Underwater Islands", "url": "/subnautica/biomes/underwater_islands/"}
    ],
    1
)

resources_list = [
    titanium,
]