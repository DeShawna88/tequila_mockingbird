from django.shortcuts import render
from rest_framework import generics
from .serializers import IngredientSerializer
from .serializers import ShoppingListSerializer
from .models import Ingredient
from .models import ShoppingList

# Create your views here.
class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all().order_by('ingredient_id')
    serializer_class = IngredientSerializer

class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all().order_by('ingredient_id')
    serializer_class = IngredientSerializer

class Shopping_ListList(generics.ListCreateAPIView):
    queryset = ShoppingList.objects.all().order_by('shopping_id')
    serializer_class = ShoppingListSerializer

class Shopping_ListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingList.objects.all().order_by('shopping_id')
    serializer_class = ShoppingListSerializer