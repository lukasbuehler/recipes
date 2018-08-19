#from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class RecipeView(TemplateView):
    template_name = 'recipe_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_id'] = self.kwargs['recipe_id']
        return context