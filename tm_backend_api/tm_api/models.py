from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    name_of_ingredient = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    recommended_drink = models.CharField(max_length=100)
    alt_ingredient = models.IntegerField(null=True, blank=True)
    is_bought = models.BooleanField()

class ShoppingList(models.Model):
    shopping_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    ingredients_list = models.ManyToManyField(Ingredient, through="ShoppingListIngredient")

class ShoppingListIngredient(models.Model):
    shopping_list = models.ForeignKey('ShoppingList', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    instructions = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredient")
    user = models.ForeignKey('User', on_delete=models.CASCADE)

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    quantity = models.IntegerField()

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    password = models.CharField(max_length=100)