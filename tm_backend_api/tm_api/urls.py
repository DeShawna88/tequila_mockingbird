from django.urls import path
from . import views

urlpatterns = [
    path('api/ingredient', views.IngredientList.as_view(), name='ingredient_list'), 
    path('api/ingredient/<int:pk>', views.IngredientDetail.as_view(), name='ingredient_detail'),
    path('api/shoppinglist', views.Shopping_ListList.as_view(), name='shoppinglist_list'),
    path('api/shoppinglist/<int:pk>', views.Shopping_ListDetail.as_view(), name='shoppinglist_detail'),
]