import imp
from django.contrib import admin
from restaurant.models import Restaurant

@admin.register(Restaurant) 
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address',)
