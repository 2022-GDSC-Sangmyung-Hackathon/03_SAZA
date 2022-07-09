from django.urls import path, include
from restaurant.views import load_restaurants_csv, update_geo

urlpatterns = [
    path('load_restaurants/', load_restaurants_csv, name='load_restaurants'),
    path('update_geo/', update_geo, name='update_geos'),
]
