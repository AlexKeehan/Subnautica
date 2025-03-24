from django.urls import path
from . import views
app_name = 'subnautica'

urlpatterns = [
    path('', views.subnautica_view, name='subnautica_view'),
    path('biomes/', views.biomes_view, name='biomes_view'),
    path('biomes/<str:biome_name>/', views.biome_view, name='biome_view'),
    path('tools/', views.tools_view, name='tools_view'),
    path('tools/<str:tool_name>/', views.tool_view, name='tool_view'),
    path('vehicles/', views.vehicles_view, name='vehicles_view'),
    path('vehicles/<str:vehicle_name>/', views.vehicle_view, name='vehicle_view'),
    path('resources/', views.resources_view, name='resources_view'),
    path('resources/<str:resource_name>/', views.resource_view, name='resource_view'),
    path('faunas/', views.faunas_view, name='faunas_view'),
    path('faunas/<str:fauna_name>/', views.fauna_view, name='fauna_view'),
    path('floras/', views.floras_view, name='floras_view'),
    path('floras/<str:flora_name>/', views.flora_view, name='flora_view'),
    path('eggs/', views.eggs_view, name='eggs_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
]