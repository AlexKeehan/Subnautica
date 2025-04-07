from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import Biomes, Resources, Floras, Faunas, Eggs, Tools, Vehicles, user, \
    admin_user

biomes_list = Biomes.objects.all()
resources_list = Resources.objects.all()
tools_list = Tools.objects.all()
vehicles_list = Vehicles.objects.all()
faunas_list = Faunas.objects.all()
floras_list = Floras.objects.all()
eggs_list = Eggs.objects.all()

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
    if request.method == "POST":
        model = request.POST.get("select_model")

        if model == "biomes":
            form = BiomesForm(request.POST)
            if form.is_valid():
                biome = form.save(commit=False)
                biome.save()

                resources = form.cleaned_data.get("resources")

                if resources:
                    biome.resources.set(resources)
                    biome.save()

                return redirect("subnautica:add_item_view")
            else:
                return render(request, 'subnautica/add_item.html', {'form': form, 'error': "Form is not valid"})
        elif model == "resources":
            form = ResourcesForm(request.POST)
            if form.is_valid():
                resource = form.save(commit=False)
                resource.save()

                biomes = form.cleaned_data.get("biomes")

                if biomes:
                    resource.biomes.set(biomes)
                    resource.save()
                return redirect("subnautica:add_item_view")
            else:
                print(form.errors)
                return render(request, 'subnautica/add_item.html', {'form': form, 'error': "Form is not valid"})
        elif model == "eggs":
            form = EggsForm(request.POST)
            if form.is_valid():
                egg = form.save(commit=False)
                egg.save()

                biomes = form.cleaned_data.get("biomes")

                if biomes:
                    egg.biomes.set(biomes)
                    egg.save()

                fauna = form.cleaned_data.get("fauna")

                if fauna:
                    egg.fauna = fauna

                egg.save()
                return redirect("subnautica:add_item_view")
            else:
                print(form.errors)
                return render(request, 'subnautica/add_item.html', {'form': form, 'error': "Form is not valid"})
        elif model == "floras":
            form = FlorasForm(request.POST)
            if form.is_valid():
                flora = form.save(commit=False)
                flora.save()

                biomes = form.cleaned_data.get("biomes")

                if biomes:
                    flora.biomes.set(biomes)
                    flora.save()
                return redirect("subnautica:add_item_view")
        elif model == "faunas":
            form = FaunasForm(request.POST)
            if form.is_valid():
                fauna = form.save(commit=False)
                fauna.save()

                biomes = form.cleaned_data.get("biomes")

                if biomes:
                    fauna.biomes.set(biomes)
                    fauna.save()
                return redirect("subnautica:add_item_view")
        elif model == "tools":
            form = ToolsForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect("subnautica:add_item_view")
        elif model == "vehicles":
            form = VehiclesForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect("subnautica:add_item_view")
        else:
            return render(request, 'subnautica/add_item.html', {'error': "Invalid Model"})

    else:
        model = request.GET.get("select_model")
        if model == "biomes":
            resources_qs = Resources.objects.all()
            form = BiomesForm()
            form.fields["resources"].queryset = resources_qs
        else:
            return render(request, 'subnautica/add_item.html', {'error': "No model selected"})

def edit_item_view(request):
    model = request.GET.get("select_model")

    if not model:
        model = request.GET.get("select_model", "biomes")

    item_id = request.GET.get("item_id")
    selected_item = None

    item_list = []

    if model == "biomes":
        item_list = biomes_list
    elif model == "faunas":
        item_list = faunas_list
    elif model == "eggs":
        item_list = eggs_list
    elif model == "floras":
        item_list = floras_list
    elif model == "vehicles":
        item_list = vehicles_list
    elif model == "tools":
        item_list = tools_list
    elif model == "resources":
        item_list = resources_list
    else:
        model = None

    if item_id:
        if model == "biomes":
            selected_item = next((item for item in biomes_list if item.get_biome_url() == item_id), None)
        elif model == "faunas":
            selected_item = next((item for item in faunas_list if item.get_fauna_url() == item_id), None)
        elif model == "eggs":
            selected_item = next((item for item in eggs_list if item.get_egg_url() == item_id), None)
        elif model == "floras":
            selected_item = next((item for item in floras_list if item.get_flora_url() == item_id), None)
        elif model == "vehicles":
            selected_item = next((item for item in vehicles_list if item.get_vehicle_url() == item_id), None)
        elif model == "tools":
            selected_item = next((item for item in tools_list if item.get_tool_url() == item_id), None)
        elif model == "resources":
            selected_item = next((item for item in resources_list if item.get_resource_url() == item_id), None)
        else:
            selected_item = None


    if request.method == "POST" and selected_item:
        if model == "biomes":
            selected_item.biome = request.POST.get("biome")
            selected_item.description = request.POST.get("description")
            selected_item.short_description = request.POST.get("short_description")
            selected_item.biome_type = request.POST.get("biome_type")
            selected_item.depth_range = request.POST.get("depth_range")
            selected_item.temp_range = request.POST.get("temp_range")
            selected_item.resources = request.POST.get("resources")

            return JsonResponse({"success": True, "message": "Biome Updated Successfully"})

    image_path = selected_item.get_img_path() if selected_item else None

    return render(request, 'subnautica/edit_item.html', {
        "model": model,
        "item_list": item_list,
        "selected_item": selected_item,
        "image_path": image_path,
    })

def del_item_view(request):
    model = request.GET.get("select_model")
    item_id = request.GET.get("item_id")
    selected_item = None
    item_list = []

    if not model:
        model = request.GET.get("select_model", "biomes")

    if model == "biomes":
        item_list = biomes_list
    elif model == "faunas":
        item_list = faunas_list
    elif model == "eggs":
        item_list = eggs_list
    elif model == "floras":
        item_list = floras_list
    elif model == "vehicles":
        item_list = vehicles_list
    elif model == "tools":
        item_list = tools_list
    elif model == "resources":
        item_list = resources_list
    else:
        model = None

    if item_id:
        if model == "biomes":
            selected_item = next((item for item in biomes_list if item.get_biome_url() == item_id), None)
        elif model == "faunas":
            selected_item = next((item for item in faunas_list if item.get_fauna_url() == item_id), None)
        elif model == "eggs":
            selected_item = next((item for item in eggs_list if item.get_egg_url() == item_id), None)
        elif model == "floras":
            selected_item = next((item for item in floras_list if item.get_flora_url() == item_id), None)
        elif model == "vehicles":
            selected_item = next((item for item in vehicles_list if item.get_vehicle_url() == item_id), None)
        elif model == "tools":
            selected_item = next((item for item in tools_list if item.get_tool_url() == item_id), None)
        elif model == "resources":
            selected_item = next((item for item in resources_list if item.get_resource_url() == item_id), None)
        else:
            selected_item = None

    if request.method == "POST" and selected_item:
        if model == "biomes":
            biomes_list.remove(selected_item)
            return JsonResponse({"success": True, "message": "Item Deleted Successfully"})
    return render(request, 'subnautica/del_item.html', {
        "model": model,
        "item_list": item_list,
        "selected_item": selected_item,
    })

def get_dropdown_data_view(request):
    model_type = request.GET.get("model")
    data = []

    if model_type == "resources":
        biomes = Biomes.objects.all()
        data = {"biomes": [{"id": biome.id, "name": biome.name} for biome in biomes]}
    elif model_type == "biomes":
        resources = Resources.objects.all()
        data = {"resources": [{"id": resource.id, "name": resource.name} for resource in resources]}
    elif model_type == "eggs":
        biomes = Biomes.objects.all()
        faunas = Faunas.objects.all()

        data = {
            "biomes": [{"id": biome.id, "name": biome.name} for biome in biomes],
            "faunas": [{"id": fauna.id, "name": fauna.name} for fauna in faunas]}
    elif model_type == "faunas":
        biomes = Biomes.objects.all()
        data = {"biomes": [{"id": biome.id, "name": biome.name} for biome in biomes]}
    elif model_type == "floras":
        biomes = Biomes.objects.all()
        data = {"biomes": [{"id": biome.id, "name": biome.name} for biome in biomes]}
    return JsonResponse(data, safe=False)