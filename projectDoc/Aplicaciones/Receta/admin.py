from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Medicamentos)
admin.site.register(Enfermedades)
admin.site.register(Alergias)
admin.site.register(Consumos)
admin.site.register(Condiciones)
admin.site.register(EnfermedadMedicamento)
admin.site.register(AlergiaMedicamento)
admin.site.register(ConsumoMedicamento)
admin.site.register(CondicionMedicamento)

