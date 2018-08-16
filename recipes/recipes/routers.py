from rest_framework import routers
from recipe.viewsets import RecipeViewSet

router = routers.DefaultRouter()

router.register(r'recipe', RecipeViewSet)