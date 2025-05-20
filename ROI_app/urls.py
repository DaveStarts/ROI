from django.urls import path
from .views import ProjektListeView, IndexView
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('rename/<str:entity_type>/<int:entity_id>/', views.rename_entity, name='rename_entity'),
    path('projekte/', ProjektListeView.as_view(), name='projekt_liste'),
]