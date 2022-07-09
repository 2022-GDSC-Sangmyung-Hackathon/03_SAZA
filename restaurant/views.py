import json
from time import sleep
from django.shortcuts import render
from numpy import append
from restaurant.models import Restaurant
from restaurant.register_functions.load_restaurants import load_restaurants_csv
from restaurant.register_functions.load_reviews import get_reviews
from restaurant.distance_functions.cal_distance import get_distance, check_1km
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView

import random
import googlemaps

googlemaps_key = "AIzaSyCfvx6iYQVGdPer3AqofpSB-jAKnw_PoVE"
gmaps = googlemaps.Client(key=googlemaps_key)

def index(request):
    context = {
        'response': 200, 
    }
    return render(request, 'restaurant/inputLocation.html', context)

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

def update_reviews(request):

    rs = Restaurant.objects.all()

    for r in rs:
        get_reviews(r.dong, r.name)

@csrf_exempt
def get_current_coordinate(request):
    coordinate = json.loads(request.body.decode('utf-8'))
    current = [coordinate['user_lat'], coordinate['user_lng']]

    print(current)

    rs = Restaurant.objects.all()

    restaurants = []

    for r in rs:
        destination = [r.latitude, r.hardness]
        distance = get_distance(current, destination)
        if check_1km(distance): 
            restaurants.append(r)

    candidate_restaurants = []
    top_10_restaurants = []
    random_20_restaurants = random.sample(restaurants, 20)

    for r in random_20_restaurants:
        try: 
            visitor_reviews, blog_reviews = get_reviews(r.dong, r.name)
            r.visitor_reviews = visitor_reviews
            r.blog_reviews = blog_reviews
            r.total_counts = visitor_reviews + blog_reviews
            r.save()

            candidate_restaurants.append(r.pk)

            if (len(candidate_restaurants) == 10): 
                break
        except:
            continue
    
    top_10_restaurants = Restaurant.objects.filter(id__in=candidate_restaurants).order_by('-total_counts')

    context = {
        'top_10_restaurants': top_10_restaurants, 
    }

    print(context)

    return render(request, 'restaurant/restaurantList.html', context)


class ResList(ListView):
    model = Restaurant

    template_name = 'restaurant/myRestaurants.html'


class ResDetail(DetailView):
    model = Restaurant

    template_name = 'restaurant/detailReview.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ResDetail, self).get_context_data()
        context['review_form'] = ReviewForm
        return  context

def index(request):
    return render(request, 'restaurant/index.html')


def myRestaurants(request):
    return render(request, 'restaurant/myRestaurants.html')
def Restaurantlist(request):
    return render(request, 'restaurant/restaurantList.html')


