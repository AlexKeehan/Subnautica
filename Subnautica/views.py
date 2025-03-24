from django.shortcuts import render
from .models import biomes_list, resources_list, floras_list, faunas_list, tools_list, vehicles_list, eggs_list


# Create your views here.
def subnautica_view(request):
    return render(request, 'subnautica/index.html')

def biomes_view(request):
    return render(request, 'subnautica/biomes.html', {"biomes_list": biomes_list})

def biome_view(request, biome_name):
    biome = next((biome for biome in biomes_list if biome.get_biome_url() == biome_name), None)

    if biome is None:
        return render(request, 'subnautica/biomes.html')

    return render(request, f'subnautica/biome_item.html', {'biome': biome})

def tools_view(request):
    return render(request, 'subnautica/tools.html', {"tools_list": tools_list})

def tool_view(request, tool_name):
    tool = next((tool for tool in tools_list if tool.get_tool_url() == tool_name), None)

    if tool is None:
        return render(request, 'subnautica/tools.html')

    return render(request, f'subnautica/tool_item.html', {'tool': tool})

def vehicles_view(request):
    return render(request, 'subnautica/vehicles.html', {"vehicles_list": vehicles_list})

def vehicle_view(request, vehicle_name):
    return render(request, f'subnautica/vehicles/{vehicle_name}.html')

def resources_view(request):
    return render(request, 'subnautica/resources.html', {"resources_list": resources_list})

def resource_view(request, resource_name):
    return render(request, f'subnautica/resources/{resource_name}.html')

def floras_view(request):
    return render(request, 'subnautica/floras.html', {"floras_list": floras_list})

def flora_view(request, flora_name):
    flora = next((flora for flora in floras_list if flora.get_flora_url() == flora_name), None)

    if flora is None:
        return render(request, 'subnautica/404.html')

    return render(request, f'subnautica/flora_item.html', {'flora': flora})

def faunas_view(request):
    return render(request, 'subnautica/faunas.html', {"faunas_list": faunas_list})

def fauna_view(request, fauna_name):
    return render(request, f'subnautica/faunas/{fauna_name}.html')

def eggs_view(request):
    return render(request, 'subnautica/eggs.html', {"eggs_list": eggs_list})

def login_view(request):
    return render(request, 'subnautica/login.html')

def signup_view(request):
    return render(request, 'subnautica/signup.html')