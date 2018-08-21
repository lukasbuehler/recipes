from rest_framework import serializers
from .models import Recipe, Step, Ingredient, IngredientCategory, Utensil, UtensilCategory

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