from django.urls import path
from . import views

urlpatterns = [
    path('api/ingredient', views.IngredientList.as_view(), name='ingredient_list'), 
    path('api/ingredient/<int:pk>', views.IngredientDetail.as_view(), name='ingredient_detail'),
    path('api/shoppinglist', views.ShoppingListList.as_view(), name='shoppinglist_list'),
    path('api/shoppinglist/<int:pk>', views.ShoppingListDetail.as_view(), name='shoppinglist_detail'),
]