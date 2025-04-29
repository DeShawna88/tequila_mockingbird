from rest_framework import serializers
from .models import Ingredient
from .models import ShoppingList

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('ingredient_id', 'name_of_ingredient', 'type', 'quantity', 'recommended_drink', 'alt_ingredient', 'is_bought',)

class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = ('shopping_id', 'name', 'ingredients_list')