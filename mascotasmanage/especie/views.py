from especie.forms import FormEspecie
from especie.models import Especie
from django.shortcuts import redirect,render
from django.contrib import messages
def menu(request):
    return render(request,'menu/menu.html')


def crearEs(request):
    form = FormEspecie()
    if request.method == 'POST':
        form= FormEspecie(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Agregado con exito")
            return redirect('/indexEs')
    data={'form': form}
    return render(request, 'especie/create.html', data)

def listaespecie(request):
    lista=Especie.objects.all()
    data={'especie':lista}
    return render(request, 'especie/indexes.html', data)







