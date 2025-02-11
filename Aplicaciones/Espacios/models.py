from django.db import models

# Create your models here.
from django.db import models

# Tabla: Áreas Públicas
class AreaPublica(models.Model):
    idAre = models.AutoField(primary_key=True)
    nombreAre = models.CharField(max_length=250)
    ubicacionAre = models.CharField(max_length=250)
    estadoAre = models.CharField(max_length=250)
    fecha_creacionAre = models.DateField()
    foto=models.FileField(upload_to='areaPublica' , null=True,blank=True)

    def __str__(self):
        return self.nombreAre


# Tabla: Proyectos de Remodelación
class Proyecto(models.Model):
    idPro = models.AutoField(primary_key=True)
    nombrePro = models.CharField(max_length=250)
    fecha_inicioPro = models.DateField()
    fecha_finPro = models.DateField()
    estadoPro = models.CharField(max_length=250)
    presupuestoPro = models.DecimalField(max_digits=10, decimal_places=2)
    foto=models.FileField(upload_to='proyecto' , null=True,blank=True)

    area_publica = models.ForeignKey(AreaPublica, on_delete=models.CASCADE, related_name='proyectos')

    def __str__(self):
        return f"Proyecto {self.idPro} - {self.area_publica.nombreAre}"


# Tabla: Contratistas
class Contratista(models.Model):
    idCon = models.AutoField(primary_key=True)
    nombreCon = models.CharField(max_length=250)
    telefonoCon = models.CharField(max_length=10)
    emailCon=models.EmailField()
    especialidadCon = models.CharField(max_length=250)
    experienciaCon = models.CharField(max_length=250)
    foto=models.FileField(upload_to='contratista' , null=True,blank=True)

    def __str__(self):
        return self.nombreCon


# Tabla: Materiales
class Material(models.Model):
    idMat = models.AutoField(primary_key=True)
    nombreMat = models.CharField(max_length=250)
    tipoMat = models.CharField(max_length=250)
    unidadMat = models.CharField(max_length=250)
    costoMat = models.DecimalField(max_digits=10, decimal_places=2)
    cantidadMat = models.CharField(max_length=250)

    def __str__(self):
        return self.nombreMat

