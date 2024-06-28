from django.db import models

# Create your models here.
class Medicamentos(models.Model):
    cNombre = models.CharField(max_length=30)
    bEstatus = models.BooleanField(default=True)

    def __str__(self):
        return self.cNombre

class Enfermedades(models.Model):
    cNombre = models.CharField(max_length=30)
    bEstatus = models.BooleanField(default=True)

    def __str__(self):
        return self.cNombre

class EnfermedadMedicamento(models.Model):
    id = models.AutoField(primary_key=True)
    IdEnfermedad = models.ForeignKey(Enfermedades, on_delete=models.CASCADE)
    IdMedicamento = models.ForeignKey(Medicamentos, on_delete=models.CASCADE)



class Alergias(models.Model):
    cNombre = models.CharField(max_length=30)
    bEstatus = models.BooleanField(default=True)

    def __str__(self):
        return self.cNombre

class AlergiaMedicamento(models.Model):
    id = models.AutoField(primary_key=True)
    IdAlergia = models.ForeignKey(Alergias, on_delete=models.CASCADE)
    IdMedicamento = models.ForeignKey(Medicamentos, on_delete=models.CASCADE)


class Condiciones(models.Model):
    cNombre = models.CharField(max_length=30)
    bEstatus = models.BooleanField(default=True)

    def __str__(self):
        return self.cNombre

class CondicionMedicamento(models.Model):
    id = models.AutoField(primary_key=True)
    IdCondicion = models.ForeignKey(Condiciones, on_delete=models.CASCADE)
    IdMedicamento = models.ForeignKey(Medicamentos, on_delete=models.CASCADE)



class Consumos(models.Model):
    cNombre = models.CharField(max_length=30)
    bEstatus = models.BooleanField(default=True)

    def __str__(self):
        return self.cNombre

class ConsumoMedicamento(models.Model):
    id = models.AutoField(primary_key=True)
    IdConsumo = models.ForeignKey(Consumos, on_delete=models.CASCADE)
    IdMedicamento = models.ForeignKey(Medicamentos, on_delete=models.CASCADE)


