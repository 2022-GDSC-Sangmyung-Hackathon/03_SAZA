from django.db import models

class Restaurant(models.Model): 
    name = models.CharField(max_length=50, verbose_name='업소명')
    address = models.CharField(max_length=100, verbose_name='도로명 주소')
    dong = models.CharField(max_length=50, verbose_name='동')
    latitude = models.FloatField(verbose_name='위도', null=True)
    hardness = models.FloatField(verbose_name='경도', null=True)
