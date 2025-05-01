from django.shortcuts import render
from rest_framework import generics
from .serializers import IngredientSerializer
from .serializers import ShoppingListSerializer
from .serializers import ShoppingListIngredientSerializer
from .serializers import RecipeSerializer
from .serializers import RecipeIngredientSerializer
from .serializers import UserSerializer
from .models import Ingredient
from .models import ShoppingList
from .models import ShoppingListIngredient
from .models import Recipe
from .models import RecipeIngredient
from .models import User

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

class Shopping_List_IngredientList(generics.ListCreateAPIView):
    queryset = ShoppingListIngredient.objects.all().order_by('id')
    serializer_class = ShoppingListIngredientSerializer

class Shopping_List_IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingListIngredient.objects.all().order_by('id')
    serializer_class = ShoppingListIngredientSerializer

class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all().order_by('recipe_id')
    serializer_class = RecipeSerializer

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all().order_by('recipe_id')
    serializer_class = RecipeSerializer

class RecipeIngredientList(generics.ListCreateAPIView):
    queryset = RecipeIngredient.objects.all().order_by('id')
    serializer_class = RecipeIngredientSerializer

class RecipeIngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecipeIngredient.objects.all().order_by('id')
    serializer_class = RecipeIngredientSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('user_id')
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('user_id')
    serializer_class = UserSerializer