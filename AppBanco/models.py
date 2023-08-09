from django.db import models
from django.db import models
from .num import Plazo
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class Cliente(models.Model):
    Documento = models.TextField(max_length=30, null=False, primary_key=True)
    Nombre = models.TextField(max_length=30)
    Apellido = models.TextField(max_length=30)
    Correo = models.TextField(max_length=30)
    Celular = models.TextField(max_length=30)
    #User = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cliente', null=True)


class User(AbstractUser):
    rol = models.CharField(max_length=100)
    imagen = models.ImageField(default='dos.png', upload_to='img/', null=True, blank=True)
    documento = models.OneToOneField(Cliente, on_delete=models.CASCADE, primary_key=True)
    #  def __str__(self):
    #  return self.username


class Lineascredito(models.Model):
    Codigo=models.PositiveSmallIntegerField(verbose_name="Codigo",primary_key=True)
    Nombre=models.TextField(max_length=30)
    Montomaxino=models.PositiveBigIntegerField(verbose_name="Monto maximo")
    Plazomaximo=models.PositiveSmallIntegerField(verbose_name="Plazo Maximo")

class Credito(models.Model):
    Documento=models.ForeignKey(Cliente, null=False,on_delete=models.CASCADE)
    Codigo=models.ForeignKey(Lineascredito, null= False,on_delete=models.CASCADE)
    Monto=models.PositiveBigIntegerField(verbose_name="Total Credito")
    Plazo=models.PositiveSmallIntegerField(verbose_name="Plazo",choices=Plazo,default=6)

class Usuario(models.Model):
    Documento=models.ForeignKey(Cliente, null=False,on_delete=models.CASCADE)
    Usuario=models.TextField(max_length=30)
    Clave=models.TextField(max_length=30)

class Empleado(models.Model):
    Documento=models.ForeignKey(Usuario, null=False,on_delete=models.CASCADE)
    Nombre=models.TextField(max_length=30)
    Apellido=models.TextField(max_length=30)
    Correo=models.TextField(max_length=30)
    Celular=models.TextField(max_length=30)
    Rol=models.TextField(max_length=30)