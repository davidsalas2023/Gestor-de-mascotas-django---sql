from django.shortcuts import redirect,render
from mascotaplus.models import Mascotas
from mascotaplus.forms import FormMascotas
from django.contrib import messages
def createmascota(request):
    form = FormMascotas()
    if request.method == 'POST':
        form= FormMascotas(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Agregado con exito")
            return redirect('/indexmas')
    data={'form': form}
    return render(request, 'mascota/create.html', data)
    




def listamascota(request):
    lista = Mascotas.objects.all()
    data = {'mascota' : lista}
    return render(request,'mascota/indexmas.html',data)

def eliminarmascota(request,id):
    va = Mascotas.objects.get(id = id)
    va.delete()
    messages.success(request,"Eliminado con exito")
    return redirect('/indexmas')

def editarmascota(request,id):
    per = Mascotas.objects.get(id=id)
    form = FormMascotas(instance=per)
    if request.method == 'POST':
        form = FormMascotas(request.POST,instance=per)
        if form.is_valid():
            form.save()
            messages.success(request,"Cambios Realizados")
            return redirect('/indexmas')
    data = {'form':form }
    return render (request,'mascota/create.html',data)


# Create your views here.
