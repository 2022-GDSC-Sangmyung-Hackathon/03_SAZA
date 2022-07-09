from django.shortcuts import render
from restaurant.models import Restaurant
from restaurant.register_functions.load_restaurants import load_restaurants_csv

import googlemaps

googlemaps_key = "AIzaSyCfvx6iYQVGdPer3AqofpSB-jAKnw_PoVE"
gmaps = googlemaps.Client(key=googlemaps_key)

def load_restaurants_csv(request):
    load_restaurants_csv()

    return render(request)

def update_geo(request):
    
    rs = Restaurant.objects.all()

    for r in rs:
        geo_location = gmaps.geocode(r.address)[0].get('geometry')
        lat = geo_location['location']['lat']
        lng = geo_location['location']['lng']

        r.latitude = lat
        r.hardness = lng 

        r.save()

    print('지리 정보가 업데이트 되었습니다.')








