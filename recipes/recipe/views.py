#from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class RecipeView(TemplateView):
    template_name = 'recipe.html'

    def get_context_data(self, **kwargs):
        context = super(RecipeView, self).get_context_data(**kwargs)
        context['id'] = '2'
        return context