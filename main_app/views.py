from audioop import reverse
from contextlib import redirect_stderr
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Breed, Breeder

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
            context["breeds"] = Breed.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["breeds"] = Breed.objects.all()  
            context["header"] = "Trending Breeds"      
        return context

class BreedCreate(CreateView):
    model = Breed
    fields = ['name', 'img', 'bio', 'verified_breed']
    template_name = "breed_create.html"
    
    def get_success_url(self):
        return reverse('breed_detail', kwargs={'pk': self.object.pk})

class BreedDetail(DetailView):
    model = Breed
    template_name = "breed_detail.html"

class BreedUpdate(UpdateView):
    model = Breed
    fields = ['name', 'img', 'bio', 'verified_breed']
    template_name = "breed_update.html"
    
    def get_success_url(self):
        return reverse('breed_detail', kwargs={'pk': self.object.pk})

class BreedDelete(DeleteView):
    model = Breed
    template_name = "breed_delete_confirmation.html"
    success_url = "/breeds/"

class BreederCreate(View):

    def post(self, request, pk):
        name = request.POST.get("name")
        breeds = request.POST.get("breeds")
        breed = Breed.objects.get(pk=pk)
        Breeder.objects.create(name=name, breeds=breeds, breed=breed)
        return redirect('breed_detail', pk=pk)

