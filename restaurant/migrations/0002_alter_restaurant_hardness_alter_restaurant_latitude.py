# Generated by Django 4.0.6 on 2022-07-09 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='hardness',
            field=models.FloatField(null=True, verbose_name='경도'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='latitude',
            field=models.FloatField(null=True, verbose_name='위도'),
        ),
    ]
