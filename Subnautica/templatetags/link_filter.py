from django import template
from django.urls import reverse

register = template.Library()

# A dictionary that maps terms to their corresponding URLs
LINKS = {
    "Blood Oil": "subnautica:resource_view",
    "Bloodroot": "subnautica:flora_view",
    # Add more mappings as needed
}

@register.filter(name='convert_to_links')
def convert_to_links(value):
    for term, url_name in LINKS.items():
        if url_name == "subnautica:resource_view":
            resource_name = term.lower().replace(" ", "_")
            url = reverse(url_name, kwargs={'resource_name': resource_name})
        elif url_name == "subnautica:flora_view":
            resource_name = term.lower().replace(" ", "_")
            url = reverse(url_name, kwargs={'flora_name': resource_name})
        link = f'<a href="{url}">{term}</a>'
        value = value.replace(term, link)
    return value

