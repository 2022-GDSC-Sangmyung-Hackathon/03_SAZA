from django.urls import path, include

from restaurant import views
from restaurant.views import index, get_current_coordinate, load_restaurants_csv, update_geo, update_reviews
from review import views as review_view

urlpatterns = [
    path('', index, name='index'), 
    path('load-restaurants/', load_restaurants_csv, name='load_restaurants'),
    path('update-geo/', update_geo, name='update_geos'),
    path('update-reviews/', update_reviews, name='update_reviews'), 
    path('get-current-coordinate/', get_current_coordinate, name='get_current_coordinate'),

    path('', views.ResList.as_view()),
    path('<int:pk>/', views.ResDetail.as_view()),

    path('<int:pk>/add_review/', review_view.add_review),
]