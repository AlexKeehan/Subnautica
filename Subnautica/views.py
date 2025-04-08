from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import Biomes, Resources, Floras, Faunas, Eggs, Tools, Vehicles, user, admin_user

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
    try:
        biome = Biomes.objects.get(name=biome_name)
    except Biomes.DoesNotExist:
        return render(request, 'subnautica/biomes.html', {'error': 'Biome not found'})

    return render(request, f'subnautica/biome_item.html', {'biome': biome})

def tools_view(request):
    return render(request, 'subnautica/tools.html', {"tools_list": tools_list})

def tool_view(request, tool_name):
    try:
        tool = Tools.objects.get(name=tool_name)
    except Tools.DoesNotExist:
        return render(request, 'subnautica/tools.html', {'error': 'Tool not found'})

    return render(request, f'subnautica/tool_item.html', {'tool': tool})

def vehicles_view(request):
    return render(request, 'subnautica/vehicles.html', {"vehicles_list": vehicles_list})

def vehicle_view(request, vehicle_name):
    try:
        vehicle = Vehicles.objects.get(name=vehicle_name)
    except Vehicles.DoesNotExist:
        return render(request, 'subnautica/vehicles.html', {'error': 'Vehicle not found'})

    return render(request, f'subnautica/vehicle_item.html', {'vehicle': vehicle})

def resources_view(request):
    return render(request, 'subnautica/resources.html', {"resources_list": resources_list})

def resource_view(request, resource_name):
    try:
        resource = Resources.objects.get(name=resource_name)
    except Resources.DoesNotExist:
        return render(request, 'subnautica/resources.html', {'error': 'Resource not found'})

    return render(request, f'subnautica/resource_item.html', {'resource': resource})

def floras_view(request):
    return render(request, 'subnautica/floras.html', {"floras_list": floras_list})

def flora_view(request, flora_name):
    try:
        flora = Floras.objects.get(name=flora_name)
    except Floras.DoesNotExist:
        return render(request, 'subnautica/floras.html', {'error': 'Flora not found'})

    return render(request, f'subnautica/flora_item.html', {'flora': flora})

def faunas_view(request):
    return render(request, 'subnautica/faunas.html', {"faunas_list": faunas_list})

def fauna_view(request, fauna_name):
    try:
        fauna = Faunas.objects.get(name=fauna_name)
    except Faunas.DoesNotExist:
        return render(request, 'subnautica/faunas.html', {'error': 'Fauna not found'})

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

                return redirect("subnautica:biome_view", biome_name=biome.name)
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
                return redirect("subnautica:resource_view", resource_name=resource.name)
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
                    try:
                        egg.fauna = fauna
                    except Faunas.DoesNotExist:
                        return render(request, 'subnautica/add_item.html', {'error': "Fauna not found"})
                egg.save()
                print(egg.fauna.name)
                return redirect("subnautica:fauna_view", fauna_name=egg.fauna.name)
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
                return redirect("subnautica:flora_view", flora_name=flora.name)
        elif model == "faunas":
            form = FaunasForm(request.POST)
            if form.is_valid():
                fauna = form.save(commit=False)
                fauna.save()

                biomes = form.cleaned_data.get("biomes")

                if biomes:
                    fauna.biomes.set(biomes)
                    fauna.save()
                return redirect("subnautica:fauna_view", fauna_name=fauna.name)
        elif model == "tools":
            form = ToolsForm(request.POST)
            if form.is_valid():
                tool = form.save()
            return redirect("subnautica:tool_view", tool_name=tool.name)
        elif model == "vehicles":
            form = VehiclesForm(request.POST)
            if form.is_valid():
                vehicle = form.save()
            return redirect("subnautica:vehicles_view", vehicle_name=vehicle.name)
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
    item_list = get_item_list(model)
    selected_item = get_selected_item(model, item_id)

    if request.method == "POST":
        item_id = request.POST.get("item_id")
        model = request.POST.get("select_model")
        selected_item = get_selected_item(model, item_id)

        if selected_item:
            if model == "biomes":
                selected_item.name = request.POST.get("name")
                selected_item.description = request.POST.get("description")
                selected_item.short_description = request.POST.get("short_description")
                selected_item.biome_type = request.POST.get("biome_type")
                selected_item.depth_range = request.POST.get("depth_range")
                selected_item.temp_range = request.POST.get("temp_range")

                resources = request.POST.getlist("resources")
                selected_item.resources.set(resources)

                selected_item.save()
                return redirect('subnautica:biome_view', biome_name=selected_item.name)
            elif model == "eggs":
                selected_item.name = request.POST.get("name")
                selected_item.description = request.POST.get("description")
                selected_item.attitude = request.POST.get("attitude")

                fauna = request.POST.get("fauna")
                if fauna:
                    selected_item.fauna = Faunas.objects.get(id=fauna)

                biomes = request.POST.getlist("biomes")
                selected_item.biomes.set(biomes)

                selected_item.save()
                return redirect('subnautica:fauna_view', fauna_name=selected_item.name)
            elif model == "floras":
                selected_item.name = request.POST.get("name")
                selected_item.description = request.POST.get("description")
                selected_item.use = request.POST.get("use")
                selected_item.attitude = request.POST.get("attitude")
                selected_item.obtain_from = request.POST.get("obtain_from")

                biomes = request.POST.getlist("biomes")
                selected_item.biomes.set(biomes)
                selected_item.growth_time = request.POST.get("growth_time")

                selected_item.save()
                return redirect('subnautica:flora_view', flora_name=selected_item.name)
            elif model == "faunas":
                selected_item.name = request.POST.get("name")
                selected_item.description = request.POST.get("description")
                selected_item.type = request.POST.get("type")
                selected_item.attitude = request.POST.get("attitude")

                biomes = request.POST.getlist("biomes")
                selected_item.biomes.set(biomes)

                selected_item.save()
                return redirect('subnautica:fauna_view', fauna_name=selected_item.name)
            elif model == "resources":
                selected_item.name = request.POST.get("name")
                selected_item.description = request.POST.get("description")
                selected_item.obtain_from = request.POST.get("obtain_from")

                biomes = request.POST.getlist("biomes")
                selected_item.biomes.set(biomes)
                selected_item.size = request.POST.get("size")

                selected_item.save()
                return redirect('subnautica:resources_view', resource_name=selected_item.name)
            elif model == "tools":
                selected_item.name = request.POST.get("name")
                selected_item.description = request.POST.get("description")
                selected_item.short_description = request.POST.get("short_description")
                selected_item.tool_type = request.POST.get("tool_type")
                selected_item.build_time = request.POST.get("build_time")
                selected_item.attribute = request.POST.get("attribute")

                selected_item.save()
                return redirect('subnautica:edit_item_view')
            elif model == "vehicles":
                selected_item.name = request.POST.get("name")
                selected_item.description = request.POST.get("description")
                selected_item.short_description = request.POST.get("short_description")
                selected_item.velocity = request.POST.get("velocity")
                selected_item.health = request.POST.get("health")
                selected_item.acq_from = request.POST.get("acq_from")

                selected_item.save()
                return redirect('subnautica:vehicle_view', vehicle_name=selected_item.name)
    image_path = selected_item.get_img_path() if selected_item else None


    return render(request, 'subnautica/edit_item.html', {
        "model": model,
        "item_list": item_list,
        "selected_item": selected_item,
        "image_path": image_path,
        "faunas": Faunas.objects.all(),
        "biomes": Biomes.objects.all(),
        "resources": Resources.objects.all(),
    })

# Helper function for editing view
# Gets the selected item based on the model and id that gets passed through POST
def get_selected_item(model, item_id):
    try:
        if model == "biomes":
            return Biomes.objects.get(pk=item_id)
        elif model == "faunas":
            return Faunas.objects.get(pk=item_id)
        elif model == "eggs":
            return Eggs.objects.get(pk=item_id)
        elif model == "floras":
            return Floras.objects.get(pk=item_id)
        elif model == "vehicles":
            return Vehicles.objects.get(pk=item_id)
        elif model == "tools":
            return Tools.objects.get(pk=item_id)
        elif model == "resources":
            return Resources.objects.get(pk=item_id)
    except Exception as e:
        print("Error fetching selected item during POST:", e)
        return None

# Helper function to get the item list from the model
# Used in editing and deleting
def get_item_list(model):
    if model == "biomes":
        return Biomes.objects.all()
    elif model == "faunas":
        return Faunas.objects.all()
    elif model == "eggs":
        return Eggs.objects.all()
    elif model == "floras":
        return Floras.objects.all()
    elif model == "vehicles":
        return Vehicles.objects.all()
    elif model == "tools":
        return Tools.objects.all()
    elif model == "resources":
        return Resources.objects.all()
    else:
        return []

def del_item_view(request):
    model = request.GET.get("select_model")
    item_id = request.GET.get("item_id")

    item_list = get_item_list(model)

    selected_item = get_selected_item(model, item_id)

    if request.method == "POST":
        item_id = request.POST.get("item_id")
        model = request.POST.get("select_model")
        item = get_selected_item(model, item_id)
        if item:
            item.delete()
            return redirect(f'subnautica:{model}_view')
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