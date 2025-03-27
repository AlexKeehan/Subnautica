from django import template
from django.urls import reverse

register = template.Library()

LINKS = {
    "Blood Oil": "subnautica:resource_view",
    "Bloodroot": "subnautica:flora_view",
    "Survival Knife": "subnautica:tool_view",
    "Ampeel": "subnautica:fauna_view",
}

@register.filter(name='convert_to_links')
def convert_to_links(value):
    for term, url_name in LINKS.items():
        if url_name == "subnautica:resource_view":
            name = term.lower().replace(" ", "_")
            url = reverse(url_name, kwargs={'resource_name': name})
        elif url_name == "subnautica:flora_view":
            name = term.lower().replace(" ", "_")
            url = reverse(url_name, kwargs={'flora_name': name})
        elif url_name == "subnautica:tool_view":
            name = term.lower().replace(" ", "_")
            url = reverse(url_name, kwargs={'tool_name': name})
        elif url_name == "subnautica:fauna_view":
            name = term.lower().replace(" ", "_")
            url = reverse(url_name, kwargs={'fauna_name': name})
        link = f'<a href="{url}">{term}</a>'
        value = value.replace(term, link)
    return value

