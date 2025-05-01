from django.contrib import admin
from .models import Ingredient
from .models import ShoppingList
from .models import ShoppingListIngredient
from .models import Recipe
from .models import RecipeIngredient
from .models import User

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(ShoppingList)
admin.site.register(ShoppingListIngredient)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(User)