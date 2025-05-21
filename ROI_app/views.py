from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import ListView, TemplateView, FormView
from .forms import ProgrammForm
from .models import Projekt, Programm, Kalkulation
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
import json

# Create your views here.
class ProjektListeView(ListView):
    model = Projekt
    template_name = 'projekt_liste.html'
    context_object_name = 'projekte'

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ProgrammForm
    success_url = reverse_lazy('index')  # Wohin nach Erfolg

    def form_valid(self, form):
        form.save()  # Speichern
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['programme'] = Programm.objects.all()
        return context

@csrf_protect
def rename_entity(request, entity_type, entity_id):

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_name = data.get('new_name')

            if entity_type == 'programm':
                obj = Programm.objects.get(pk=entity_id)
            elif entity_type == 'kalk':
                obj = Kalkulation.objects.get(pk=entity_id)
            else:
                return JsonResponse({'success': False, 'error': 'Ungültiger Typ'}, status=400)

            obj.name = new_name
            obj.save()

            return JsonResponse({'success': True, 'new_name': new_name})
        
        except Programm.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Programm nicht gefunden'}, status=404)
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)
