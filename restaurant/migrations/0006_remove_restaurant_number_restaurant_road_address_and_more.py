# Generated by Django 4.0.6 on 2022-07-09 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_rename_gu_restaurant_dong'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='number',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='road_address',
            field=models.CharField(default=1, max_length=100, verbose_name='도로명 주소'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(max_length=100, verbose_name='지번주소'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=50, verbose_name='업소명'),
        ),
    ]
