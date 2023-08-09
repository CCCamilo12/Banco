from django.contrib import admin
from AppBanco.models import *
@admin.register(Cliente)
class Clienteadmin(admin.ModelAdmin):
    list_display=('Documento','Nombre','Apellido','Correo','Celular')
    #ordering=('-Nombre',)
    #ordering=('Nombre','Apellido')
    #list_display_links=('Documento',)
    #search_fields=('Documento','Nombre')
    #list_editable=('Documento','Nombre','Apellido','Correo','Edad')
    #list_filter=('nombre',)
    list_per_page=2
    
@admin.register(Lineascredito)
class Lineaadmin(admin.ModelAdmin):
    list_display=('Codigo','Nombre','Montomaxino','Plazomaximo') 

    
@admin.register(Credito)
class Creditoadmin(admin.ModelAdmin):
    list_display=('Documento','Codigo','Monto','Plazo') 
# Register your models here.

@admin.register(Usuario)
class Usuarioadmin(admin.ModelAdmin):
    list_display=('Documento','Usuario','Clave') 

@admin.register(Empleado)
class Empleadoadmin(admin.ModelAdmin):
    list_display=('Documento','Nombre','Apellido','Correo','Celular','Rol') 