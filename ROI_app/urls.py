from django.urls import path
from .views import ProjektListeView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('projekte/', ProjektListeView.as_view(), name='projekt_liste'),
]