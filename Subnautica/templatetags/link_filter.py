from django import template
from django.urls import reverse

register = template.Library()

LINKS = {
    "Blood Oil": "subnautica:resource_view",
    "Bloodroot": "subnautica:flora_view",
    "Survival Knife": "subnautica:tool_view",
    "Ampeel": "subnautica:fauna_view",
    "Blood Kelp Caves": "subnautica:biome_view",
    "Safe Shallows": "subnautica:biome_view",
    "Grassy Plateaus": "subnautica:biome_view",
}

@register.filter(name='convert_to_links')
def convert_to_links(value):
    for term, url_name in LINKS.items():
        if url_name == "subnautica:resource_view":
            url = reverse(url_name, kwargs={'resource_name': url_name})
        elif url_name == "subnautica:flora_view":
            url = reverse(url_name, kwargs={'flora_name': url_name})
        elif url_name == "subnautica:tool_view":
            url = reverse(url_name, kwargs={'tool_name': url_name})
        elif url_name == "subnautica:fauna_view":
            url = reverse(url_name, kwargs={'fauna_name': url_name})
        elif url_name == "subnautica:biome_view":
            url = reverse(url_name, kwargs={'biome_name': url_name})
        link = f'<a href="{url}">{term}</a>'
        value = value.replace(term, link)
    return value

