# Generated by Django 2.1 on 2018-08-19 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_title',
            new_name='title',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipeToMake',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='recipe.Recipe'),
        ),
    ]
