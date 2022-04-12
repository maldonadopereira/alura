from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('importa_transacao', views.importa_transacao, name='importa_transacao')
]