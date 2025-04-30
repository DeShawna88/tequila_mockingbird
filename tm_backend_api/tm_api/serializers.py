from rest_framework import serializers
from .models import Ingredient
from .models import ShoppingList
from .models import Recipe
from .models import RecipeIngredient
from .models import User

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('ingredient_id', 'name_of_ingredient', 'type', 'quantity', 'recommended_drink', 'alt_ingredient', 'is_bought',)

class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = ('shopping_id', 'name', 'ingredients_list')

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('recipe_id', 'name', 'instructions', 'ingredients', 'user')

class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = ('recipe', 'ingredient', 'quantity')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'name', 'email', 'address', 'phone_number', 'shopping_id')