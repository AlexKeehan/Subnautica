from django import forms
from .models import *

class BiomesForm(forms.ModelForm):
    resources = forms.ModelMultipleChoiceField(
        queryset=Resources.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'dropdown'}),
        required=False
    )
    class Meta:
        model = Biomes
        fields = ["name", "description", "short_description", "biome_type", "depth_range", "temp_range", "resources"]

class ResourcesForm(forms.ModelForm):
    biomes = forms.ModelMultipleChoiceField(
        queryset=Biomes.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'dropdown'}),
        required=False
    )
    class Meta:
        model = Resources
        fields = ["name", "description", "obtain_from", "biomes", "size"]

class EggsForm(forms.ModelForm):
    fauna = forms.ModelChoiceField(
        queryset=Faunas.objects.all(),
        widget=forms.Select(attrs={'class': 'dropdown'}),
        required=False
    )
    biomes = forms.ModelMultipleChoiceField(
        queryset=Biomes.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'dropdown'}),
        required=False
    )
    class Meta:
        model = Eggs
        fields = ["name", "description", "attitude", "fauna", "biomes"]

class FaunasForm(forms.ModelForm):
    biomes = forms.ModelMultipleChoiceField(
        queryset=Biomes.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'dropdown'}),
        required=False
    )
    class Meta:
        model = Faunas
        fields = ["name", "description", "fauna_type", "attitude", "biomes"]

class FlorasForm(forms.ModelForm):
    biomes = forms.ModelMultipleChoiceField(
        queryset=Biomes.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'dropdown'}),
        required=False
    )
    class Meta:
        model = Floras
        fields = ["name", "description", "use", "attitude", "obtain_from", "biomes", "growth_time"]

class ToolsForm(forms.ModelForm):
    class Meta:
        model = Tools
        fields = ["name", "description", "short_description", "tool_type", "build_time", "attribute"]

class VehiclesForm(forms.ModelForm):
    class Meta:
        model = Vehicles
        fields = ["name", "description", "short_description", "velocity", "health", "acq_from"]