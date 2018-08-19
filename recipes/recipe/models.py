from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class UtensilCategory(models.Model):
    name = models.CharField(max_length=250)


class Utensil(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(UtensilCategory, on_delete=models.CASCADE)




class Action(models.Model):
    description = models.CharField(max_length=250)
    verb = models.CharField(max_length=50)
    utensil = models.ForeignKey(Utensil, on_delete=models.CASCADE, null=True)

class IngredientCategory(models.Model):
    name = models.CharField(max_length=250)

class Ingredient(models.Model):
    name = models.CharField(max_length=250)
    #category = models.ForeignKey(IngredientCategory, on_delete=models.CASCADE)
    #recipeToMake = models.ForeignKey(Recipe, blank=True, on_delete=models.CASCADE)
    



class Step(models.Model):
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=True)
    amount = models.FloatField(null=True)


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    #author = 
    #category = 
    description = models.TextField()
    rating = models.FloatField(
        null=True,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    forAmountOfPersons = models.PositiveSmallIntegerField(
        default=4,
        validators=[
            MinValueValidator(1)
        ]
    )
    steps = models.ManyToManyField(Step)
    #ingredients = 

