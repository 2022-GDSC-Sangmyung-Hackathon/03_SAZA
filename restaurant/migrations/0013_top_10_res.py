# Generated by Django 4.0.6 on 2022-07-09 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0012_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='TOP_10_RES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list', models.CharField(max_length=100, verbose_name='상위 10위 음식점 pk값')),
            ],
        ),
    ]
