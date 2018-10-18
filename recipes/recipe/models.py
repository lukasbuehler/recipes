from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class UtensilCategory(models.Model):
    name = models.CharField(max_length=250)


class Utensil(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(UtensilCategory, on_delete=models.CASCADE)


class IngredientCategory(models.Model):
    name = models.CharField(max_length=250)

class Ingredient(models.Model):
    name = models.CharField(max_length=250)
    #category = models.ForeignKey(IngredientCategory, on_delete=models.CASCADE)
    #recipeToMake = models.ForeignKey(Recipe, blank=True, on_delete=models.CASCADE)


class Step(models.Model):
    text = models.CharField(max_length=100, null=True)
    vars = models.CharField(max_length=10000, null=True)

    def __str__(self):
        return self.text

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    #author = 
    #category = 
    image = models.ImageField(upload_to="images/recipes/", null=True)
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

    def __str__(self):
        return self.title+" ("+str(self.id)+")"

    