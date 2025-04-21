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
    path('search/', views.search_view, name='search_view'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('manage_users/', views.manage_users_view, name='manage_users_view'),
    path('update_user_role/<int:user_id>/', views.update_user_role_view, name='update_user_role_view'),
    path('user_index/', views.user_index_view, name='user_index_view'),
    path('admin_dashboard/', views.admin_user_view, name='admin_user_view'),
    path('add_item/', views.add_item_view, name='add_item_view'),
    path('edit_item/', views.edit_item_view, name='edit_item_view'),
    path('del_item/', views.del_item_view, name='del_item_view'),
    path('get_dropdown_data/', views.get_dropdown_data_view, name='get_dropdown_data_view'),
]