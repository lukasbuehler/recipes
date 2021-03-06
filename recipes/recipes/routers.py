from rest_framework import routers, filters
from recipe.viewsets import RecipeViewSet, StepViewSet, IngredientViewSet, IngredientCategoryViewSet, UtensilViewSet, UtensilCategoryViewSet, RecipeUserViewSet

router = routers.DefaultRouter()

router.register(r'recipe', RecipeViewSet)
router.register(r'step', StepViewSet)
router.register(r'ingredient', IngredientViewSet)
router.register(r'ingredient_category', IngredientCategoryViewSet)
router.register(r'utensil', UtensilViewSet)
router.register(r'utensil_category', UtensilCategoryViewSet)

router.register(r'user', RecipeUserViewSet)