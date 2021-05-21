from django.shortcuts import render

from .models import Metahumano
# Create your views here.


def listado_metahumans(request):
    filas = Metahumano.objects.all()
    return render(request, 'metahumans/listado.html', {
        "filas": filas,
    })
