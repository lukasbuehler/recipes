from rest_framework import viewsets
from .models import Recipe, Step, Action, Ingredient, IngredientCategory, Utensil, UtensilCategory
from .serializers import RecipeSerializer, StepSerializer, ActionSerializer, IngredientSerializer, IngredientCategorySerializer, UtensilSerializer, UtensilCategorySerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientCategoryViewSet(viewsets.ModelViewSet):
    queryset = IngredientCategory.objects.all()
    serializer_class = IngredientCategorySerializer

class UtensilViewSet(viewsets.ModelViewSet):
    queryset = Utensil.objects.all()
    serializer_class = UtensilSerializer

class UtensilCategoryViewSet(viewsets.ModelViewSet):
    queryset = UtensilCategory.objects.all()
    serializer_class = UtensilCategorySerializer
