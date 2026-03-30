from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Registro

@login_required
def lista(request):
    registros = Registro.objects.all()
    return render(request, 'registros/lista.html', {'registros': registros})

@login_required
def agregar(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        Registro.objects.create(nombre=nombre, descripcion=descripcion)
        return redirect('lista')
    return render(request, 'registros/agregar.html')

@login_required
def eliminar(request, id):
    registro = get_object_or_404(Registro, id=id)
    registro.delete()
    return redirect('lista')

@login_required
def editar(request, id):
    registro = get_object_or_404(Registro, id=id)
    if request.method == 'POST':
        registro.nombre = request.POST['nombre']
        registro.descripcion = request.POST['descripcion']
        registro.save()
        return redirect('lista')
    return render(request, 'registros/editar.html', {'registro': registro})