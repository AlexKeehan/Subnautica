class Tools:
    def __init__(self, tool, description, short_description, type, build_time, attribute):
        self.tool = tool
        self.description = description
        self.short_description = short_description
        self.type = type
        self.build_time = build_time
        self.attribute = attribute

    def get_img_name(self):
        return self.tool.lower().replace(" ", "_") + ".webp"

    def get_tool_url(self):
        return self.tool.lower().replace(" ", "_")

    def get_img_path(self):
        return f"img/Tools/{self.get_img_name()}"

air_bladder = Tools(
    "Air Bladder",
    """
    The Air Bladder is a tool crafted from the Fabricator.
    It is a flotation device that produces a chemical reaction that allows the player to reach the surface faster than by simply swimming.
    """,
    "Emergency flotation device. When activated, it produces a chemical reaction that provides buoyancy.",
    "Utility",
    "3 seconds",
    "Buoyancy"
)

tools_list = [
    air_bladder,
]