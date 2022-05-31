from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Breed

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class BreedList(TemplateView):
    template_name = "breed_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["breeds"] = Breed.objects.filter(name_icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["breeds"] = Breed.objects.all()  
            context["header"] = "Trending Breeds"      
        return context
