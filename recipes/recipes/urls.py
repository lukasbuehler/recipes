"""recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from dhango.contrib.auth import urls
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView
from recipe.views import RecipeView
from .routers import router




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path('', TemplateView.as_view(template_name='feed.html')),

    path('recipe_list/', TemplateView.as_view(template_name='recipe_list.html')),
    
    path('recipes/', TemplateView.as_view(template_name='recipes.html')),
    path('recipe/<int:recipe_id>/', RecipeView.as_view(), name="recipe_details"),

    path('accounts/', include('django.contrib.auth.urls')),

    path('u/<username>/', TemplateView.as_view(template_name='profile.html')),
    path('u/<username>/recipes/', TemplateView.as_view(template_name='recipes.html')),

    path('u/id/<int:user_id>/recipes/', TemplateView.as_view(template_name='recipes.html'))
    
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
