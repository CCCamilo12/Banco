from atexit import register
from pydoc import cli
from typing import Any
from django.shortcuts import render
from AppBanco.models import *
from django.views.generic import *
from django.http import *
from django.utils.decorators import *
from django.views.decorators.csrf import *
import json  

  
def principal (request):
    listaclientes=Cliente.objects.all()
    return render(request,"index.html",{"Cli":listaclientes})


""" class ListadoClientes(ListView):
    model=Cliente
    template_name="index.html" """

""" 
class Listadolineacredito(ListView):
    model=Lineascredito
    template_name="indexuno.html" """

""" class Listadocredito(ListView):
    model=Credito
    template_name="indexdos.html"

class Listadousuarios(ListView):
    model=Usuario
    template_name="indextres.html" """

""" class Listadoempleado(ListView):
    model=Empleado
    template_name="indexcuatro.html" """
    
""" class ListadoClientes(ListView):
    def get(self,request):
        datos=Cliente.objects.all().
        datos_Cliente=[]
        for i in datos:
            datos_Cliente.append({
                'Documento':i.Documento,
                'Nombre':i.Nombre,
                'Apellido':i.Apellido,
                'Correo':i.Correo,
                'Celular':i.Celular

            })
        return JsonResponse(datos_Cliente, safe=False) """
class ListadoClientes(View):
    def get(self,request):
        datos=Cliente.objects.all().values()
        datoscli=list(datos)
        return render(request,'index.html',{'datos':datoscli})




class Insertarcliente(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args, **kwargs):
        return super().dispatch(request, *args, **kwargs)  
    def post(self,request):
        try:
            datos=json.loads(request.body)
        except(json.JSONDecodeError,UnicodeDecodeError):
            return JsonResponse({"Error":"Error"})
        Documento = datos.get('Documento')
        Nombre = datos.get('Nombre')
        Apellido = datos.get('Apellido')
        Correo = datos.get('Correo')
        Celular = datos.get('Celular')
        cli=Cliente.objects.create(Documento=Documento,Nombre=Nombre,Apellido=Apellido,Correo=Correo,Celular=Celular,)
        cli.save()
        #return JsonResponse({'Mensaje':'datos guardados'})   
        #return render(request,"formulario.html",{'mensaje':'Datos guardados'})
        return JsonResponse({"mensaje":"Datos Guardados"})

class Actualizar(View):            
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def put(self, request,pk):
            
        try:
            registro=Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return JsonResponse({"Error":"El documento no existe"})
        data=json.loads(request.body)
        registro.Nombre=data.get('Nombre')
        registro.Apellido=data.get('Apellido')
        registro.Correo=data.get('Correo')
        registro.Celular=data.get('Celular')
        registro.save()
        return JsonResponse({"Mensaje":"Datos Actualizados"})
    
class Eliminar(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def delete(self,request,pk):
        try:
            registro=Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return JsonResponse({"Error":"El documento no existe"})
        registro.delete()
        return JsonResponse({"Mensaje":"Datos Eliminados"})
    

def formularioInsertar(request):
    return render(request,"formulario.html")


                