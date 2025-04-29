from django.contrib import admin
from .models import Ingredient
from .models import ShoppingList

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(ShoppingList)