from rest_framework import serializers
from .models import (
        Ingredient,
        ShoppingList,
        ShoppingListIngredient,
        Recipe,
        RecipeIngredient,
        User,
    )
from django.contrib.auth.hashers import make_password


class IngredientSerializer(serializers.ModelSerializer):
        class Meta:
            model = Ingredient
            fields = ('ingredient_id', 'name_of_ingredient', 'type', 'recommended_drink', 'alt_ingredient', 'is_bought', 'user')


class ShoppingListSerializer(serializers.ModelSerializer):
        class Meta:
            model = ShoppingList
            fields = ('shopping_id', 'name', 'user', 'ingredients_list')


class ShoppingListIngredientSerializer(serializers.ModelSerializer):
        class Meta:
            model = ShoppingListIngredient
            fields = ('id', 'shopping_list', 'ingredient', 'quantity')


class RecipeSerializer(serializers.ModelSerializer):
        class Meta:
            model = Recipe
            fields = ('recipe_id', 'name', 'instructions', 'ingredients', 'user')


class RecipeIngredientSerializer(serializers.ModelSerializer):
        class Meta:
            model = RecipeIngredient
            fields = ('id', 'recipe', 'ingredient', 'quantity')


class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('user_id', 'email', 'name', 'phone_number', 'address')
            read_only_fields = ('user_id',)


class UserCreateSerializer(serializers.ModelSerializer):
        password = serializers.CharField(write_only=True, style={'input_type': 'password'})

        class Meta:
            model = User
            fields = ('user_id', 'email', 'name', 'password', 'phone_number', 'address')
            read_only_fields = ('user_id',)

        def create(self, validated_data):
            password = validated_data.pop('password')
            user = User(**validated_data)
            user.password = make_password(password)
            user.save()
            return user

        def update(self, instance, validated_data):
            password = validated_data.pop('password', None)
            if password is not None:
                instance.password = make_password(password) # change to make_password

            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()
            return instance
    