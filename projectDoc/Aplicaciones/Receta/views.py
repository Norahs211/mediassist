from django.shortcuts import render, redirect
from .models import * #Enfermedades, Medicamentos, EnfermedadMedicamento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.views.generic import RedirectView
from django.urls import reverse_lazy

#me traigo los registro de las tablas catalogos para llenar las tablas donde se seleccionaran
# para ver que medicamentos les corresponde
@login_required()
def seleccionar(request):
    enfermedades = Enfermedades.objects.all() #enfermedades
    alergias = Alergias.objects.all() #alergias
    condiciones = Condiciones.objects.all() #condiones
    consumos = Consumos.objects.all() #consumos
    return render(request, 'seleccionar.html', {'enfermedades': enfermedades, 'alergias': alergias,
                                                'condiciones': condiciones, 'consumos': consumos})

@login_required()
def consulta_medicamentos(request):
    if request.method == 'POST':
        #enfermedades
        id_enfermedades = request.POST.getlist('enfermedades', []) or [] # Obtener una lista de IDs de enfermedades seleccionadas o una lista vacia si no se selcciono nada
        medicamentos = Medicamentos.objects.filter(enfermedadmedicamento__IdEnfermedad_id__in=id_enfermedades).distinct() # Filtrar medicamentos basados en las enfermedades seleccionadas

        #alergias
        id_alergias = request.POST.getlist('alergias', []) or []
        MEdicamentos = Medicamentos.objects.filter(alergiamedicamento__IdAlergia_id__in=id_alergias).distinct()

        #condiciones
        id_condiciones = request.POST.getlist('condiciones', []) or []
        MEDIcamentos = Medicamentos.objects.filter(condicionmedicamento__IdCondicion_id__in=id_condiciones).distinct()

        #consumos
        id_consumos = request.POST.getlist('consumos', []) or []
        MEDICAmentos = Medicamentos.objects.filter(consumomedicamento__IdConsumo_id__in=id_consumos).distinct()

        return render(request, 'medicamentos.html', {'medicamentos': medicamentos, 'MEdicamentos': MEdicamentos,
                                                     'MEDIcamentos': MEDIcamentos, 'MEDICAmentos': MEDICAmentos})
    else:
        return render(request, 'seleccionar.html')

class SalirView(RedirectView):
    url = reverse_lazy('login')  # URL a la que se redirigirá después de cerrar sesión

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)

