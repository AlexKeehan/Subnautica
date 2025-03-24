class Biomes:
    def __init__(self, biome, description, short_description, biome_type, depth_range, temp_range, resources):
        self.biome = biome
        self.description = description
        self.short_description = short_description
        self.biome_type = biome_type
        self.depth_range = depth_range
        self.temp_range = temp_range
        self.resources = resources

    def get_img_name(self):
        return self.biome.lower().replace(" ", "_") + ".webp"

    def get_biome_url(self):
        return self.biome.lower().replace(" ", "_")

    def get_img_path(self):
        return f"img/Biomes/{self.get_img_name()}"

blood_kelp_caves = Biomes(
    "Blood Kelp Caves",
    """
    This biome is known for its eerie atmosphere and its abundance of large <a href="{% url 'subnautica:flora_view' flora_name='bloodroots' %}">Bloodroots</a> 
    that grow on every surface and carry large pustules of <a href="{% url 'subnautica:resource_view' resource_name='blood_oil' %}">Blood Oil</a>.
    These caves also offer extensive bioluminescent flora and rock formations.
    """,
    """
    These caves are characterized by Bloodroots that grow large pustules of Blood Oil
    """,
    "Cave",
    "285-675 meters",
    "13.5°C-14.3°C",
[
    {"name": "Blood Oil", "url": "/subnautica/resources/blood_oil/"},
    {"name": "Diamond", "url": "/subnautica/resources/diamond/"},
    {"name": "Ghost Weed Seed", "url": "/subnautica/floras/ghost_weed_seed/"},
    {"name": "Gold", "url": "/subnautica/resources/gold/"},
    {"name": "Large Copper Deposit", "url": "/subnautica/resources/large_copper_dep/"},
    {"name": "Large Gold Deposit", "url": "/subnautica/resources/large_gold_dep/"},
    {"name": "Large Uranium Deposit", "url": "/subnautica/resources/large_uranium_dep/"},
    {"name": "Lithium", "url": "/subnautica/resources/lithium/"},
    {"name": "Quartz", "url": "/subnautica/resources/quartz/"},
    {"name": "Uraninite Crystal", "url": "/subnautica/resources/uraninite_crystal/"},
    {"name": "Magnetite", "url": "/subnautica/resources/magnetite/"}]
)

blood_kelp_zone = Biomes(
    "Blood Kelp Zone",
    """
    This biome is characterized by its depth, darkness, eerie environment, and giant <a href="../Flora/bloodvine.html">Bloodvines</a>.
                <a href="../Flora/blood_oil.html">Blood Oil</a> can be found in pustules growing from the stems of the <a href="../Flora/bloodvines.html">Bloodvines</a>.
                <br/><br/>
                This biome is split into two sections, one being the Blood Kelp Trench located in the south-west and the second being the Northern Blood Kelp Zone.
                The trench is a deep split in the ground that has depths reaching almost 700 meters.
                It is a very tight confined space that offers significant resources for those brave enough.
                <br/><br/>
                The Northern Blood Kelp Zone layout varies significantly from the Trench, with it being a sprawling deep biome that offers significant threats and resources.
                An entrance to a mysterious and deadly biome can be found in the depths of this biome.
    """,
    """
    This biome is known for its depth, darkness and abundance of Bloodvines and Blood Oil.
    """,
    "Surface",
    "150 - 675 meters (Trench)\n"
    "200 - 580 meters (Northern)",
    "13.5&deg;C-14.3&deg;C (Trench)\n"
    "13.6&deg;C-14.2&deg;C (Northern)",
[
    {"name": "Ampeel Egg", "url": "/subnautica/fauna/ampeel/"},
    {"name": "Blood Oil", "url": "/subnautica/resources/blood_oil/"},
    {"name": "Crabsquid Egg", "url": "/subnautica/fauna/crabsquid/"},
    {"name": "Deep Shroom", "url": "/subnautica/floras/deep_shroom/"},
    {"name": "Diamond", "url": "/subnautica/resources/diamond/"},
    {"name": "Gel Sack", "url": "/subnautica/floras/gel_sack/"},
    {"name": "Ghost Weed Seed", "url": "/subnautica/floras/ghost_weed_seed/"},
    {"name": "Gold", "url": "/subnautica/resources/gold/"},
    {"name": "Large Copper Deposit", "url": "/subnautica/resources/large_copper_dep/"},
    {"name": "Large Gold Deposit", "url": "/subnautica/resources/large_gold_dep/"},
    {"name": "Large Lead Deposit", "url": "/subnautica/resources/large_lead_dep/"},
    {"name": "Lithium", "url": "/subnautica/resources/lithium/"},
    {"name": "Magnetite", "url": "/subnautica/resources/magnetite/"},
    {"name": "Quartz", "url": "/subnautica/resources/quartz/"},
    {"name": "Ruby", "url": "/subnautica/resources/ruby/"},
    {"name": "Salt Deposit", "url": "/subnautica/resources/salt_dep/"},
    {"name": "Uraninite Crystal", "url": "/subnautica/resources/uraninite_crystal/"}]
)

safe_shallows = Biomes(
"Safe Shallows",
    """
    The Safe Shallows is the starter biome for new players and contains sprawling coral reefs and small cave systems. 
    As the name implies, this shallow biome is one of the safest in the game, with no predatory creatures. However, there are environmental hazards and it is quite easy to be disoriented by the winding caves and run out of oxygen.
    Some predators can wander into this biome from the <a href="../kelp_forest">Kelp Forest</a> and <a href="../grassy_plateaus">Grassy Plateaus</a>.
    <br /><br />
    This biome offers plentiful diving experiences for new players, with a variety of floras, faunas, and resources. At night time, this biome truly shows its alien nature with plentiful bioluminescence.
    """,
    """
    The Safe Shallows is the starter biome for new players.
    """,
    "Surface",
    "0-80 meters",
    "26.5°C-32°C",
    [
    {"name": "Acid Mushroom", "url": "/subnautica/floras/acid_mushroom/"},
    {"name": "Copper Ore", "url": "/subnautica/resources/copper_ore/"},
    {"name": "Coral Tube Sample", "url": "/subnautica/floras/coral_tube_sample/"},
    {"name": "Gas Pod", "url": "/subnautica/resources/gas_pod/"},
    {"name": "Gasopod Egg", "url": "/subnautica/faunas/gasopod/"},
    {"name": "Gold", "url": "/subnautica/resources/gold/"},
    {"name": "Lead", "url": "/subnautica/resources/lead/"},
    {"name": "Metal Salvage", "url": "/subnautica/resources/metal_salvage/"},
    {"name": "Quartz", "url": "/subnautica/resources/quartz/"},
    {"name": "Rabbit Ray Egg", "url": "/subnautica/faunas/rabbit_ray/"},
    {"name": "Silver Ore", "url": "/subnautica/resources/silver_ore/"},
    {"name": "Table Coral Sample", "url": "/subnautica/floras/table_coral_sample/"},
    {"name": "Titanium", "url": "/subnautica/resources/titanium/"}]
)

biomes_list = [
    blood_kelp_caves,
    blood_kelp_zone,
    safe_shallows,
]
