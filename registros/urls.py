from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name='lista'),
    path('agregar/', views.agregar, name='agregar'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('registro/', views.registro_usuario, name='registro'),
    path('importar/', views.importar_excel, name='importar'),
    path('descargar-plantilla/', views.descargar_plantilla, name='descargar_plantilla'),
    path('eliminar-masivo/', views.eliminar_masivo, name='eliminar_masivo'),
]
