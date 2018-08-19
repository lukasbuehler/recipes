from django.db import models

# Create your models here.
class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    text = models.TextField()


class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    recipeToMake = models.ForeignKey(Recipe, blank=True, on_delete=models.CASCADE)
    
