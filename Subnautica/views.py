from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import Biomes, Resources, Floras, Faunas, Eggs, Tools, Vehicles, Users

# Base view
def subnautica_view(request):
    return render(request, 'subnautica/index.html')

def biomes_view(request):
    sort_by = request.GET.get('sort_by', None)
    order = request.GET.get('order', 'asc')

    if sort_by == "alphabet":
        if order == "asc":
            biomes_list = Biomes.objects.all().order_by('name')
        else:
            biomes_list = Biomes.objects.all().order_by('-name')
    elif sort_by == "count":
        if order == "asc":
            biomes_list = Biomes.objects.all().annotate(num_items=models.Count("resources")).order_by('num_items')
        else:
            biomes_list = Biomes.objects.all().annotate(num_items=models.Count("resources")).order_by('-num_items')
    else:
        biomes_list = Biomes.objects.all()
    return render(request, 'subnautica/biomes.html', {"biomes_list": biomes_list})

def biome_view(request, biome_name):
    try:
        biome = Biomes.objects.get(name=biome_name)
    except Biomes.DoesNotExist:
        return render(request, 'subnautica/biomes.html', {'error': 'Biome not found'})

    return render(request, f'subnautica/biome_item.html', {'biome': biome})

def tools_view(request):
    sort_by = request.GET.get('sort_by', None)
    order = request.GET.get('order', 'asc')

    if sort_by == "alphabet":
        if order == "asc":
            tools_list = Tools.objects.all().order_by('name')
        else:
            tools_list = Tools.objects.all().order_by('-name')
    else:
        tools_list = Tools.objects.all()
    return render(request, 'subnautica/tools.html', {"tools_list": tools_list})

def tool_view(request, tool_name):
    try:
        tool = Tools.objects.get(name=tool_name)
    except Tools.DoesNotExist:
        return render(request, 'subnautica/tools.html', {'error': 'Tool not found'})

    return render(request, f'subnautica/tool_item.html', {'tool': tool})

def vehicles_view(request):
    sort_by = request.GET.get('sort_by', None)
    order = request.GET.get('order', 'asc')

    if sort_by == "alphabet":
        if order == "asc":
            vehicles_list = Vehicles.objects.all().order_by('name')
        else:
            vehicles_list = Vehicles.objects.all().order_by('-name')
    else:
        vehicles_list = Vehicles.objects.all()
    return render(request, 'subnautica/vehicles.html', {"vehicles_list": vehicles_list})

def vehicle_view(request, vehicle_name):
    try:
        vehicle = Vehicles.objects.get(name=vehicle_name)
    except Vehicles.DoesNotExist:
        return render(request, 'subnautica/vehicles.html', {'error': 'Vehicle not found'})

    return render(request, f'subnautica/vehicle_item.html', {'vehicle': vehicle})

def resources_view(request):
    sort_by = request.GET.get('sort_by', None)
    order = request.GET.get('order', 'asc')

    if sort_by == "alphabet":
        if order == "asc":
            resources_list = Resources.objects.all().order_by('name')
        else:
            resources_list = Resources.objects.all().order_by('-name')
    elif sort_by == "count":
        if order == "asc":
            resources_list = Resources.objects.all().annotate(num_items=models.Count("biomes")).order_by('num_items')
        else:
            resources_list = Resources.objects.all().annotate(num_items=models.Count("biomes")).order_by('-num_items')
    else:
        resources_list = Resources.objects.all()
    return render(request, 'subnautica/resources.html', {"resources_list": resources_list})

def resource_view(request, resource_name):
    try:
        resource = Resources.objects.get(name=resource_name)
    except Resources.DoesNotExist:
        return render(request, 'subnautica/resources.html', {'error': 'Resource not found'})

    return render(request, f'subnautica/resource_item.html', {'resource': resource})

def floras_view(request):
    sort_by = request.GET.get('sort_by', None)
    order = request.GET.get('order', 'asc')

    if sort_by == "alphabet":
        if order == "asc":
            floras_list = Floras.objects.all().order_by('name')
        else:
            floras_list = Floras.objects.all().order_by('-name')
    elif sort_by == "count":
        if order == "asc":
            floras_list = Floras.objects.all().annotate(num_items=models.Count("biomes")).order_by('num_items')
        else:
            floras_list = Floras.objects.all().annotate(num_items=models.Count("biomes")).order_by('-num_items')
    else:
        floras_list = Floras.objects.all()
    return render(request, 'subnautica/floras.html', {"floras_list": floras_list})

def flora_view(request, flora_name):
    try:
        flora = Floras.objects.get(name=flora_name)
    except Floras.DoesNotExist:
        return render(request, 'subnautica/floras.html', {'error': 'Flora not found'})

    return render(request, f'subnautica/flora_item.html', {'flora': flora})

def faunas_view(request):
    sort_by = request.GET.get('sort_by', None)
    order = request.GET.get('order', 'asc')

    if sort_by == "alphabet":
        if order == "asc":
            faunas_list = Faunas.objects.all().order_by('name')
        else:
            faunas_list = Faunas.objects.all().order_by('-name')
    elif sort_by == "count":
        if order == "asc":
            faunas_list = Faunas.objects.all().annotate(num_items=models.Count("biomes")).order_by('num_items')
        else:
            faunas_list = Faunas.objects.all().annotate(num_items=models.Count("biomes")).order_by('-num_items')
    else:
        faunas_list = Faunas.objects.all()
    return render(request, 'subnautica/faunas.html', {"faunas_list": faunas_list})

def fauna_view(request, fauna_name):
    try:
        fauna = Faunas.objects.get(name=fauna_name)
    except Faunas.DoesNotExist:
        return render(request, 'subnautica/faunas.html', {'error': 'Fauna not found'})

    return render(request, f'subnautica/fauna_item.html', {'fauna': fauna})

def eggs_view(request):
    sort_by = request.GET.get('sort_by', None)
    order = request.GET.get('order', 'asc')

    if sort_by == "alphabet":
        if order == "asc":
            eggs_list = Eggs.objects.all().order_by('name')
        else:
            eggs_list = Eggs.objects.all().order_by('-name')
    elif sort_by == "count":
        if order == "asc":
            eggs_list = Eggs.objects.all().annotate(num_items=models.Count("biomes")).order_by('num_items')
        else:
            eggs_list = Eggs.objects.all().annotate(num_items=models.Count("biomes")).order_by('-num_items')
    else:
        eggs_list = Eggs.objects.all()
    return render(request, 'subnautica/eggs.html', {"eggs_list": eggs_list})

def search_view(request):
    query = request.GET.get('query', '')

    # Assume that biome is the only thing to search for
    if query:
        filtered_items = Biomes.objects.filter(name__icontains=query)
    else:
        filtered_items = Biomes.objects.all()

    return render(request, 'subnautica/search_results.html', {'query': query, 'biomes': filtered_items})

def login_view(request):
    # If form is submitted
    if request.method == "POST":
        # Get credentials
        username = request.POST.get("username")
        pw = request.POST.get("password")

        try:
            user = Users.objects.get(username=username)
        except Users.DoesNotExist:
            return render(request, 'subnautica/login.html', {'error': 'Username not found'})

        if user.check_password(pw):

            request.session["username"] = user.username
            if user.is_staff:
                request.session["role"] = "admin"
                return redirect('subnautica:admin_user_view')
            else:
                request.session["role"] = "user"
                return redirect('subnautica:user_index_view')

        return render(request,"subnautica/login.html", {'error_msg': 'Password not found'})
    # Form is not submitted, so just show login page
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

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        played_game = request.POST.get("played_game") == 'on'
        is_staff = request.POST.get("is_staff") == 'on'

        user = Users.objects.create_user(username=username,
                                         email=email,
                                         password=password,
                                         first_name=first_name,
                                         last_name=last_name,
                                         played_game=played_game,
                                         is_staff=is_staff)

        request.session["username"] = user.username
        if user.is_staff:
            request.session["role"] = "admin"
            return redirect('subnautica:admin_user_view')
        else:
            request.session["role"] = "user"
            return redirect('subnautica:user_index_view')
    else:
        return render(request, 'subnautica/signup.html')

def manage_users_view(request):
    if not request.session["role"] == "admin":
        return redirect('subnautica:user_index_view')
    users = Users.objects.all()
    return render(request, 'subnautica/manage_users.html', {'users': users})

def update_user_role_view(request, user_id):
    if request.method == "POST":
        if not request.session["role"] == "admin":
            return redirect('subnautica:user_index_view')

        try:
            user = Users.objects.get(id=user_id)
        except Users.DoesNotExist:
            return redirect('subnautica:manage_users_view')

        new_role = request.POST.get("new_role")
        if new_role == "admin":
            user.is_staff = True
        else:
            user.is_staff = False

        user.save()

        return redirect('subnautica:manage_users_view')
    else:
        return redirect('subnautica:manage_users_view')

# View that handles adding new item logic
def add_item_view(request):
    # If form is submitted
    if request.method == "POST":
        # Get model
        model = request.POST.get("select_model")

        # Use Biomes as base model
        if not model:
            model = request.GET.get("select_model", "biomes")

        # Check for which model it is
        if model == "biomes":
            # Get form
            form = BiomesForm(request.POST)
            if form.is_valid():
                # Save new data
                biome = form.save(commit=False)
                biome.save()

                # Handle ManyToMany relationship seperate
                resources = form.cleaned_data.get("resources")

                if resources:
                    biome.resources.set(resources)
                    biome.save()

                # Send success message
                messages.success(request, f"Biome {biome.name} has been added")

                # Redirect to new page
                return redirect("subnautica:biome_view", biome_name=biome.name)
            else:
                return render(request, 'subnautica/add_item.html', {'form': form, 'error': f"Form not valid: \n{form.errors}"})
        elif model == "resources":
            # Get form
            form = ResourcesForm(request.POST)
            if form.is_valid():
                resource = form.save(commit=False)
                resource.save()

                # Handle biomes seperate
                biomes = form.cleaned_data.get("biomes")

                if biomes:
                    resource.biomes.set(biomes)
                    resource.save()

                # Send success message
                messages.success(request, f"Resource {resource.name} has been added")

                # Redirect to new page
                return redirect("subnautica:resource_view", resource_name=resource.name)
            else:
                return render(request, 'subnautica/add_item.html',{'form': form, 'error': f"Form not valid: \n{form.errors}"})
        elif model == "eggs":
            # Get form
            form = EggsForm(request.POST)
            if form.is_valid():
                egg = form.save(commit=False)
                egg.save()

                # Handle biomes seperate
                biomes = form.cleaned_data.get("biomes")

                if biomes:
                    egg.biomes.set(biomes)
                    egg.save()

                # Handle fauna seperate
                fauna = form.cleaned_data.get("fauna")

                if fauna:
                    try:
                        egg.fauna = fauna
                    except Faunas.DoesNotExist:
                        return render(request, 'subnautica/add_item.html', {'error': "Fauna not found"})
                egg.save()

                # Send success message
                messages.success(request, f"Egg {egg.name} has been added")

                # Redirect to new page
                return redirect("subnautica:fauna_view", fauna_name=egg.fauna.name)
            else:
                return render(request, 'subnautica/add_item.html', {'form': form, 'error': f"Form not valid: \n{form.errors}"})
        elif model == "floras":
            # Get form
            form = FlorasForm(request.POST)
            if form.is_valid():
                flora = form.save(commit=False)
                flora.save()

                # Handle seperate
                biomes = form.cleaned_data.get("biomes")

                if biomes:
                    flora.biomes.set(biomes)
                    flora.save()

                # Send success message
                messages.success(request, f"Flora {flora.name} has been added")

                # Redirect to new page
                return redirect("subnautica:flora_view", flora_name=flora.name)
            else:
                return render(request, 'subnautica/add_item.html', {'form': form, 'error': f"Form not valid: \n{form.errors}"})
        elif model == "faunas":
            # Get form
            form = FaunasForm(request.POST)
            if form.is_valid():
                fauna = form.save(commit=False)
                fauna.save()

                # Handle seperate
                biomes = form.cleaned_data.get("biomes")

                if biomes:
                    fauna.biomes.set(biomes)
                    fauna.save()

                # Send success message
                messages.success(request, f"Fauna {fauna.name} has been added")

                # Redirect to new page
                return redirect("subnautica:fauna_view", fauna_name=fauna.name)
            else:
                return render(request, 'subnautica/add_item.html',{'form': form, 'error': f"Form not valid: \n{form.errors}"})
        elif model == "tools":
            # Get form
            form = ToolsForm(request.POST)
            if form.is_valid():
                tool = form.save()

                # Send success message
                messages.success(request, f"Tool {tool.name} has been added")

                # Redirect to new page
                return redirect("subnautica:tool_view", tool_name=tool.name)
            else:
                return render(request, 'subnautica/add_item.html',{'form': form, 'error': f"Form not valid: \n{form.errors}"})
        elif model == "vehicles":
            # Get form
            form = VehiclesForm(request.POST)
            if form.is_valid():
                vehicle = form.save()

                # Send success message
                messages.success(request, f"Vehicle {vehicle.name} has been added")

                # Redirect to new page
                return redirect("subnautica:vehicles_view", vehicle_name=vehicle.name)
            else:
                return render(request, 'subnautica/add_item.html',{'form': form, 'error': f"Form not valid: \n{form.errors}"})
        else:
            return render(request, 'subnautica/add_item.html')
    else:
        # Have biomes be the default model shown
        model = request.GET.get("select_model")
        if model == "biomes":
            resources_qs = Resources.objects.all()
            form = BiomesForm()
            form.fields["resources"].queryset = resources_qs
        else:
            return render(request, 'subnautica/add_item.html')

# View to handle editing of an existing item
def edit_item_view(request):
    # Get model
    model = request.GET.get("select_model")

    # Let Biomes be the default model shown
    if not model:
        model = request.GET.get("select_model", "biomes")

    # Get item id and then use helper functions to get items associated with that model and the specific item from that item id
    item_id = request.GET.get("item_id")
    item_list = get_item_list(model)
    selected_item = get_selected_item(model, item_id)

    if request.method == "POST":
        # Refresh these because they don't carry over
        item_id = request.POST.get("item_id")
        model = request.POST.get("select_model")
        selected_item = get_selected_item(model, item_id)

        if selected_item:
            # Check which model the selected item falls within
            if model == "biomes":
                # Set new data
                selected_item.name = request.POST.get("name")
                selected_item.description = request.POST.get("description")
                selected_item.short_description = request.POST.get("short_description")
                selected_item.biome_type = request.POST.get("biome_type")
                selected_item.depth_range = request.POST.get("depth_range")
                selected_item.temp_range = request.POST.get("temp_range")

                resources = request.POST.getlist("resources")
                selected_item.resources.set(resources)

                selected_item.save()

                # Send info message
                messages.info(request, f"Biome {selected_item.name} has been successfully edited")

                # Redirect to edited page
                return redirect('subnautica:biome_view', biome_name=selected_item.name)
            elif model == "eggs":
                # Set new data
                selected_item.name = request.POST.get("name")
                selected_item.description = request.POST.get("description")
                selected_item.attitude = request.POST.get("attitude")

                fauna = request.POST.get("fauna")
                if fauna:
                    selected_item.fauna = Faunas.objects.get(id=fauna)

                biomes = request.POST.getlist("biomes")
                selected_item.biomes.set(biomes)

                selected_item.save()

                # Send info message
                messages.info(request, f"Egg {selected_item.name} has been successfully edited")

                # Redirect to edited page
                return redirect('subnautica:fauna_view', fauna_name=selected_item.name)
            elif model == "floras":
                # Set new data
                selected_item.name = request.POST.get("name")
                selected_item.description = request.POST.get("description")
                selected_item.use = request.POST.get("use")
                selected_item.attitude = request.POST.get("attitude")
                selected_item.obtain_from = request.POST.get("obtain_from")

                biomes = request.POST.getlist("biomes")
                selected_item.biomes.set(biomes)
                selected_item.growth_time = request.POST.get("growth_time")

                selected_item.save()

                # Send info message
                messages.info(request, f"Flora {selected_item.name} has been successfully edited")

                # Redirect to edited page
                return redirect('subnautica:flora_view', flora_name=selected_item.name)
            elif model == "faunas":
                # Set new data
                selected_item.name = request.POST.get("name")
                selected_item.description = request.POST.get("description")
                selected_item.type = request.POST.get("type")
                selected_item.attitude = request.POST.get("attitude")

                biomes = request.POST.getlist("biomes")
                selected_item.biomes.set(biomes)

                selected_item.save()

                # Send info message
                messages.info(request, f"Fauna {selected_item.name} has been successfully edited")

                # Redirect to edited page
                return redirect('subnautica:fauna_view', fauna_name=selected_item.name)
            elif model == "resources":
                # Set new data
                selected_item.name = request.POST.get("name")
                selected_item.description = request.POST.get("description")
                selected_item.obtain_from = request.POST.get("obtain_from")

                biomes = request.POST.getlist("biomes")
                selected_item.biomes.set(biomes)
                selected_item.size = request.POST.get("size")

                selected_item.save()

                # Send info message
                messages.info(request, f"Resource {selected_item.name} has been successfully edited")

                # Redirect to edited page
                return redirect('subnautica:resource_view', resource_name=selected_item.name)
            elif model == "tools":
                # Set new data
                selected_item.name = request.POST.get("name")
                selected_item.description = request.POST.get("description")
                selected_item.short_description = request.POST.get("short_description")
                selected_item.tool_type = request.POST.get("tool_type")
                selected_item.build_time = request.POST.get("build_time")
                selected_item.attribute = request.POST.get("attribute")

                selected_item.save()

                # Send info message
                messages.info(request, f"Tool {selected_item.name} has been successfully edited")

                # Redirect to edited page
                return redirect('subnautica:edit_item_view')
            elif model == "vehicles":
                # Set new data
                selected_item.name = request.POST.get("name")
                selected_item.description = request.POST.get("description")
                selected_item.short_description = request.POST.get("short_description")
                selected_item.velocity = request.POST.get("velocity")
                selected_item.health = request.POST.get("health")
                selected_item.acq_from = request.POST.get("acq_from")

                selected_item.save()

                # Send info message
                messages.info(request, f"Vehicle {selected_item.name} has been successfully edited")

                # Redirect to edited page
                return redirect('subnautica:vehicle_view', vehicle_name=selected_item.name)
            else:
                return render(request, 'subnautica/edit_item.html', {'error': "Model not found"})
        else:
            return render(request, 'subnautica/edit_item.html', {'error': "Item not found"})

    # Image path is separate from an item's model
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

# View to handling deleting an item
def del_item_view(request):
    # Get model
    model = request.GET.get("select_model")

    # Let biomes be the default model shown
    if not model:
        model = request.GET.get("select_model", "biomes")

    # Get info for chosen item to display
    item_id = request.GET.get("item_id")
    item_list = get_item_list(model)
    selected_item = get_selected_item(model, item_id)

    if request.method == "POST":
        # Get info again because it may have changed
        item_id = request.POST.get("item_id")
        model = request.POST.get("select_model")
        item = get_selected_item(model, item_id)
        if item:
            # Delete item
            item.delete()

            # Send warning message
            messages.warning(request, f"Item {item.name} has been successfully deleted")

            # Redirect to list page for deleted item
            return redirect(f'subnautica:{model}_view')
        else:
            return render(request, 'subnautica/del_item.html', {'error': "Item not found"})
    return render(request, 'subnautica/del_item.html', {
        "model": model,
        "item_list": item_list,
        "selected_item": selected_item,
    })

# Used in adding an item to dynamically display data for an item
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