from django.urls import path, include
from restaurant.views import get_current_coordinate, load_restaurants_csv, update_geo, update_reviews

urlpatterns = [
    path('load-restaurants/', load_restaurants_csv, name='load_restaurants'),
    path('update-geo/', update_geo, name='update_geos'),
    path('update-reviews/', update_reviews, name='update_reviews'), 
    path('get-current-coordinate/', get_current_coordinate, name='get_current_coordinate'), 
]
