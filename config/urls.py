from django.contrib import admin
from django.urls import path, include

from review import views
from restaurant import views as res_views

urlpatterns = [
    path('', res_views.index),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('restaurant/', include('restaurant.urls')),

    # path('<int:pk>/add_review/', views.add_review),

    path('mypage/', views.mypage),
    path('detailreview/', views.detailReview),
    path('index/', views.index),
    path('inputReview/', views.inputReview),

    path('myrestaurants/', res_views.myRestaurants),
    path('restaurantList/', res_views.Restaurantlist),
]