from django.urls import path
from . import views

urlpatterns = [
    path('ingredient', views.IngredientList.as_view(), name='ingredient_list'),
    path('ingredient/<int:pk>', views.IngredientDetail.as_view(), name='ingredient_detail'),
    path('shoppinglist', views.Shopping_ListList.as_view(), name='shoppinglist_list'),
    path('shoppinglist/<int:pk>', views.Shopping_ListDetail.as_view(), name='shoppinglist_detail'),
    path('recipe', views.RecipeList.as_view(), name='recipe_list'),
    path('recipe/<int:pk>', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('recipeingredient', views.RecipeIngredientList.as_view(), name='recipeingredient_list'),
    path('recipeingredient/<int:pk>', views.RecipeIngredientDetail.as_view(), name='recipeingredient_detail'),
    path('user', views.UserList.as_view(), name='user_list'),
    path('user/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
]