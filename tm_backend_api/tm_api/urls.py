from django.urls import path
from . import views

urlpatterns = [
    path('api/ingredient', views.IngredientList.as_view(), name='ingredient_list'), 
    path('api/ingredient/<int:pk>', views.IngredientDetail.as_view(), name='ingredient_detail'),
    path('api/shoppinglist', views.Shopping_ListList.as_view(), name='shoppinglist_list'),
    path('api/shoppinglist/<int:pk>', views.Shopping_ListDetail.as_view(), name='shoppinglist_detail'),
    path('api/shoppinglistingredient', views.Shopping_List_IngredientList.as_view(), name='shoppinglistingredient_list'),
    path('api/shoppinglistingredient/<int:pk>', views.Shopping_List_IngredientDetail.as_view(), name='shoppinglistingredient_detail'),
    path('api/recipe', views.RecipeList.as_view(), name='recipe_list'),
    path('api/recipe/<int:pk>', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('api/recipeingredient', views.RecipeIngredientList.as_view(), name='recipeingredient_list'),
    path('api/recipeingredient/<int:pk>', views.RecipeIngredientDetail.as_view(), name='recipeingredient_detail'),
    path('api/user', views.UserList.as_view(), name='user_list'),
    path('api/user/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
]