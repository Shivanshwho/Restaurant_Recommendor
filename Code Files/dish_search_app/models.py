from django.db import models

class Dish(models.Model):
    restaurant_id = models.CharField(max_length=1000)
    restaurant_name = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    items = models.JSONField()

    class Meta:
        app_label = 'dish_search_app'