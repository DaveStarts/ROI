from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Projekt, Programm

# Create your views here.

class ProjektListeView(ListView):
    model = Projekt
    template_name = 'projekt_liste.html'
    context_object_name = 'projekte'

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['programme'] = Programm.objects.all()
        return context