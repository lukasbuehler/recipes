from rest_framework import viewsets
from filters.mixins import (
    FiltersMixin,
)
import django_filters.rest_framework
from .models import Recipe, Step, Ingredient, IngredientCategory, Utensil, UtensilCategory, RecipeUser

from django.contrib.auth.models import User

from .serializers import RecipeSerializer, StepSerializer, IngredientSerializer, IngredientCategorySerializer, UtensilSerializer, UtensilCategorySerializer, RecipeUserSerializer


class RecipeViewSet(FiltersMixin, viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    #filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)

    filter_mappings = {
        'creator': 'creator'
    }

class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer

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


class RecipeUserViewSet(FiltersMixin, viewsets.ModelViewSet):
    queryset = RecipeUser.objects.all()
    serializer_class = RecipeUserSerializer

    #filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)

    filter_mappings = {
        'username': 'user__username'
    }
