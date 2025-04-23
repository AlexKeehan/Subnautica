from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import *
from .models.activity import Activity
from .models.replies import Reply


# Make forms for all models for easier data handling
class BiomesForm(forms.ModelForm):
    resources = forms.ModelMultipleChoiceField(
        queryset=Resources.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "dropdown"}),
        required=False
    )
    class Meta:
        model = Biomes
        fields = ["name", "description", "short_description", "biome_type", "depth_range", "temp_range", "resources"]

class ResourcesForm(forms.ModelForm):
    biomes = forms.ModelMultipleChoiceField(
        queryset=Biomes.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "dropdown"}),
        required=False
    )
    class Meta:
        model = Resources
        fields = ["name", "description", "obtain_from", "biomes", "size"]

class EggsForm(forms.ModelForm):
    fauna = forms.ModelChoiceField(
        queryset=Faunas.objects.all(),
        widget=forms.Select(attrs={"class": "dropdown"}),
        required=False
    )
    biomes = forms.ModelMultipleChoiceField(
        queryset=Biomes.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "dropdown"}),
        required=False
    )
    class Meta:
        model = Eggs
        fields = ["name", "description", "attitude", "fauna", "biomes"]

class FaunasForm(forms.ModelForm):
    biomes = forms.ModelMultipleChoiceField(
        queryset=Biomes.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "dropdown"}),
        required=False
    )
    class Meta:
        model = Faunas
        fields = ["name", "description", "fauna_type", "attitude", "biomes"]

class FlorasForm(forms.ModelForm):
    biomes = forms.ModelMultipleChoiceField(
        queryset=Biomes.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "dropdown"}),
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

class ProfileForm(UserChangeForm):
    class Meta:
        model = Users
        fields = ["username", "first_name", "last_name", "email", "played_game"]
        widgets = {
            "played_game": forms.Select(choices=[(True, "Yes"), (False, "No")]),
        }

    new_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={"placeholder": "Leave blank to keep same password"}),
        label="New password"
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("new_password")
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"placeholder": "Leave a comment...", "rows": 3, "cols": 60}),
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"placeholder": "Write reply here", "required": True}),
        }

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ["user", "action_type", "item_type", "item_name", "related_comment"]
        widgets = {
            "user": forms.HiddenInput(),
            "action_type": forms.HiddenInput(),
            "item_type": forms.HiddenInput(),
            "item_name": forms.HiddenInput(),
            "related_comment": forms.HiddenInput(),
        }
