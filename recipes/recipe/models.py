from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    recipe_title = models.CharField(max_length=250)
    recipe_text = models.TextField()