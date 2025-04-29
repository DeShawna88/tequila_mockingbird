from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Ingredient(models.Model):
    ingredient_ID = models.AutoField(primary_key=True)
    name_of_ingredient = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    quantity = models.IntegerField()
    recommended_drink = models.CharField(max_length=100)
    alt_ingredient = models.IntegerField()
    is_bought = models.BooleanField()

class ShoppingList(models.Model):
    shopping_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    ingredients_list = ArrayField(models.CharField(max_length=300),blank=True,null=True)