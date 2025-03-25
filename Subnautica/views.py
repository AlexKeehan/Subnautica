from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .models import biomes_list, resources_list, floras_list, faunas_list, tools_list, vehicles_list, eggs_list, user, admin_user


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
    vehicle = next((vehicle for vehicle in vehicles_list if vehicle.get_vehicle_url() == vehicle_name), None)

    if vehicle is None:
        return render(request, 'subnautica/vehicles.html')

    return render(request, f'subnautica/vehicle_item.html', {'vehicle': vehicle})

def resources_view(request):
    return render(request, 'subnautica/resources.html', {"resources_list": resources_list})

def resource_view(request, resource_name):
    resource = next((resource for resource in resources_list if resource.get_resource_url() == resource_name), None)

    if resource is None:
        return render(request, 'subnautica/resources.html')

    return render(request, f'subnautica/resource_item.html', {'resource': resource})

def floras_view(request):
    return render(request, 'subnautica/floras.html', {"floras_list": floras_list})

def flora_view(request, flora_name):
    flora = next((flora for flora in floras_list if flora.get_flora_url() == flora_name), None)

    if flora is None:
        return render(request, 'subnautica/floras.html')

    return render(request, f'subnautica/flora_item.html', {'flora': flora})

def faunas_view(request):
    return render(request, 'subnautica/faunas.html', {"faunas_list": faunas_list})

def fauna_view(request, fauna_name):
    fauna = next((fauna for fauna in faunas_list if fauna.get_fauna_url() == fauna_name), None)

    if fauna is None:
        return render(request, 'subnautica/faunas.html')

    return render(request, f'subnautica/fauna_item.html', {'fauna': fauna})

def eggs_view(request):
    return render(request, 'subnautica/eggs.html', {"eggs_list": eggs_list})

def search_view(request):
    query = request.GET.get('query', '')

    filtered_biomes = [biome for biome in biomes_list if query.lower() in biome.biome.lower()]

    return render(request, 'subnautica/search_results.html', {'query': query, 'biomes': filtered_biomes})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pw = request.POST.get("password")
        if username == user["username"] and pw == user["password"]:
            request.session["username"] = username
            request.session["role"] = "user"
            return redirect("subnautica:user_index_view")
        elif username == admin_user["username"] and pw == admin_user["password"]:
            request.session["username"] = username
            request.session["role"] = "admin"
            return redirect("subnautica:admin_user_view")
        else:
            return render(request, 'subnautica/login.html', {"error_msg": "Invalid username or password"})
    else:
        return render(request, 'subnautica/login.html')

def user_index_view(request):
    return render(request, 'subnautica/index_user.html')

def admin_user_view(request):
    return render(request, 'subnautica/admin_dashboard.html')

def logout_view(request):
    del request.session["username"]
    del request.session["role"]
    return redirect('subnautica:subnautica_view')

def signup_view(request):
    return render(request, 'subnautica/signup.html')

def add_item_view(request):
    return render(request, 'subnautica/add_item.html')

def edit_item_view(request):
    return render(request, 'subnautica/edit_item.html')

def del_item_view(request):
    return render(request, 'subnautica/del_item.html')