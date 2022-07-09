from pyexpat import model
from django.db import models

class Restaurant(models.Model): 
    name = models.CharField(max_length=50, verbose_name='업소명')
    address = models.CharField(max_length=100, verbose_name='도로명 주소')
    dong = models.CharField(max_length=50, verbose_name='동')
    latitude = models.FloatField(verbose_name='위도', null=True)
    hardness = models.FloatField(verbose_name='경도', null=True)
    visitor_reviews = models.IntegerField(verbose_name='방문자 리뷰수')
    blog_reviews = models.IntegerField(verbose_name='블로그 리뷰수')
    total_counts = models.IntegerField(verbose_name='전체 리뷰수')