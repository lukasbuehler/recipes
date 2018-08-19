from rest_framework import routers
from recipe.viewsets import RecipeViewSet, StepViewSet, ActionViewSet, IngredientViewSet, IngredientCategoryViewSet, UtensilViewSet, UtensilCategoryViewSet

router = routers.DefaultRouter()

router.register(r'recipe', RecipeViewSet)
router.register(r'step', StepViewSet)
router.register(r'action', ActionViewSet)
router.register(r'ingredient', IngredientViewSet)
router.register(r'ingredient_category', IngredientCategoryViewSet)
router.register(r'utensil', UtensilViewSet)
router.register(r'utensil_category', UtensilCategoryViewSet)