from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Recipe, Step, Ingredient, IngredientCategory, Utensil, UtensilCategory, RecipeUser

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class IngredientCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientCategory
        fields = '__all__'

class UtensilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utensil
        fields = '__all__'

class UtensilCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UtensilCategory
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RecipeUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = RecipeUser
        fields = '__all__'