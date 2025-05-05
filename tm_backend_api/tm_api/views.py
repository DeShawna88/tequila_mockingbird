from rest_framework import generics, status
from rest_framework.views import APIView, Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from .serializers import (
    IngredientSerializer,
    ShoppingListSerializer,
    ShoppingListIngredientSerializer,
    RecipeSerializer,
    RecipeIngredientSerializer,
    UserSerializer,
    UserCreateSerializer,
)
from .models import (
    Ingredient,
    ShoppingList,
    ShoppingListIngredient,
    Recipe,
    RecipeIngredient,
    User,
)

@api_view(['POST'])
@permission_classes([AllowAny])
def user_registration_view(request):  # Changed function name to snake_case
    """
    Register a new user.
    """
    serializer = UserCreateSerializer(data=request.data)  # Use UserCreateSerializer
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': UserSerializer(user).data  # Use UserSerializer for response
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def user_login_view(request):  # Added login view
    """
    Log in a user.
    """
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        return Response({
            'token': token.key,
            'user': serializer.data
        }, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout_view(request):  # Changed to snake_case
    """
    Log out the current user.
    """
    try:
        request.user.auth_token.delete()
    except AttributeError:
        pass # If the user does not have an auth_token
    return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)



@api_view(['GET'])
def api_root(request):
    """
    API root view.
    """
    return Response({"message": "Welcome to the Tequila Mockingbird API!"})



class UserList(generics.ListAPIView):  # Changed to ListAPIView and renamed
    """
    View for listing all users.  Only for admin use (if needed).
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  #  Add permission


class UserDetail(generics.RetrieveUpdateAPIView): # Changed Class Name
    """
    View for retrieving and updating the current user's details.
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Return the current user.
        """
        return self.request.user

class IngredientList(generics.ListCreateAPIView):
    """
    View for listing and creating ingredients for the current user.
    """
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return a list of ingredients for the current user.
        """
        return Ingredient.objects.filter(user=self.request.user).order_by('ingredient_id')

    def perform_create(self, serializer):
        """
        Create a new ingredient for the current user.
        """
        serializer.save(user=self.request.user)


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a single ingredient
    for the current user.
    """
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return a single ingredient for the current user.
        """
        return Ingredient.objects.filter(user=self.request.user).order_by('ingredient_id')



class Shopping_ListList(generics.ListCreateAPIView): # Changed Class Name
    """
    View for listing and creating shopping lists for the current user.
    """
    serializer_class = ShoppingListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return a list of shopping lists for the current user.
        """
        return ShoppingList.objects.filter(user=self.request.user).order_by('shopping_id')

    def perform_create(self, serializer):
        """
        Create a new shopping list for the current user.
        """
        serializer.save(user=self.request.user)  # Assign the current user



class Shopping_ListDetail(generics.RetrieveUpdateDestroyAPIView): # Changed Class Name
    """
    View for retrieving, updating, and deleting a single shopping list
    for the current user.
    """
    serializer_class = ShoppingListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return a single shopping list for the current user.
        """
        return ShoppingList.objects.filter(user=self.request.user).order_by('shopping_id')



class Shopping_List_IngredientList(generics.ListCreateAPIView): # Changed Class Name
    """
    View for listing and creating ingredients in a shopping list.
    """
    serializer_class = ShoppingListIngredientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return shopping list ingredients for the user's shopping lists.
        """
        return ShoppingListIngredient.objects.filter(shopping_list__user=self.request.user).order_by('id')

    def perform_create(self, serializer):
        """
        Create a new shopping list ingredient.
        """
        #  Get the shopping list id from the request data
        shopping_list_id = self.request.data.get('shopping_list')
        if not shopping_list_id:
            raise ValueError("Shopping list ID is required")
        # Get the shopping list object and validate if the user has access to it.
        shopping_list = get_object_or_404(ShoppingList, id=shopping_list_id, user=self.request.user)

        serializer.save(shopping_list=shopping_list)


class Shopping_List_IngredientDetail(generics.RetrieveUpdateDestroyAPIView): # Changed Class Name
    """
    View for retrieving, updating, and deleting a single shopping list ingredient.
    """
    serializer_class = ShoppingListIngredientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return a single shopping list ingredient for the user's shopping lists.
        """
        return ShoppingListIngredient.objects.filter(shopping_list__user=self.request.user).order_by('id')

class Shopping_List_IngredientList(generics.ListCreateAPIView):
    queryset = ShoppingListIngredient.objects.all().order_by('id')
    serializer_class = ShoppingListIngredientSerializer

class Shopping_List_IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingListIngredient.objects.all().order_by('id')
    serializer_class = ShoppingListIngredientSerializer

class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all().order_by('recipe_id')
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return a list of recipes for the current user.
        """
        return Recipe.objects.filter(user=self.request.user).order_by('recipe_id')

    def perform_create(self, serializer):
        """
        Create a new recipe for the current user.
        """
        serializer.save(user=self.request.user)



class RecipeDetail(generics.RetrieveUpdateDestroyAPIView): # Changed Class Name
    """
    View for retrieving, updating, and deleting a single recipe
    for the current user.
    """
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return a single recipe for the current user.
        """
        return Recipe.objects.filter(user=self.request.user).order_by('recipe_id')



class RecipeIngredientList(generics.ListCreateAPIView): # Changed Class Name
    """
    View for listing and creating ingredients in a recipe.
    """
    serializer_class = RecipeIngredientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return recipe ingredients for the user's recipes.
        """
        return RecipeIngredient.objects.filter(recipe__user=self.request.user).order_by('id')

    def perform_create(self, serializer):
        """
        Create a new recipe ingredient.
        """
        #  Get the recipe id from the request
        recipe_id = self.request.data.get('recipe')
        if not recipe_id:
            raise ValueError("Recipe ID is required")
         # Get the recipe object and validate if the user has access to it.
        recipe = get_object_or_404(Recipe, id=recipe_id, user=self.request.user)
        serializer.save(recipe=recipe)



class RecipeIngredientDetail(generics.RetrieveUpdateDestroyAPIView): # Changed Class Name
    """
    View for retrieving, updating, and deleting a single recipe ingredient.
    """
    serializer_class = RecipeIngredientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return a single recipe ingredient for the user's recipes.
        """
        return RecipeIngredient.objects.filter(recipe__user=self.request.user).order_by('id')

