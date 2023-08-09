from django.shortcuts import render, redirect
from django.views import View
from .forms import *

from django.contrib.auth import *
from django.views import View
from django.utils.decorators import *
from django.views.decorators.csrf import *
from typing import Any
from django.contrib import messages
import json
from .formscliente import ClienteForm
from .models import *


class RegistrasUsuariosView(View):
    template_name = 'login.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        form = UserForm()  # Definir form con un valor predeterminado
        if request.method == 'POST':
            print("en el metodod")
            #if request.headers.get('content-type') == 'application/json':
            if 'application/json' in request.headers.get('content-type', ''):
                print("en el json")
                self.handle_flutter_data(request)
            else:
                print("no json")
                form = UserForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Usuario registrado correctamente desde formulario HTML.')
                    return redirect('iniciar_sesion')
                else:
                    messages.error(request, 'Error al registrar el usuario desde formulario HTML.')
        else:
            print("no metodo")
            form = UserForm()
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        form = UserForm()
        return render(request, self.template_name, {'form': form})

    def handle_flutter_data(self, request):
        try:
            data = json.loads(request.body)
            print("Datos recibidos desde Flutter:")
            print(data)  # Imprime los datos recibidos desde Flutter
            form = UserForm(data)
            if form.is_valid():
                print("Datos válidos:")
                print(form.cleaned_data)  # Imprime los datos validados por el formulario
                form.save()
                messages.success(request, 'Usuario registrado correctamente desde Flutter.')
            else:
                print("Errores en el formulario:")
                print(form.errors)  # Imprime los errores de validación del formulario
        except json.JSONDecodeError:
            messages.error(request, 'Error en los datos enviados desde Flutter.')
    
class IniciarSesionView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'iniciosesion.html', {'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            datt = authenticate(username=username, password=password)

            if datt is not None:
                login(request, datt)

                if datt.rol == 'cliente':
                    try:
                        documento = datt.documento_id
                        print("DDDDDDDDDDDDDDD",documento)
                        cliente = Cliente.objects.get(documento=documento)
                        if request.method == 'POST' and 'editar' in request.POST:
                            print("Entrando a clientes Post")
                            cliente_form = ClienteForm(request.POST, instance =cliente)
                            if cliente_form.is_valid():
                                cliente_form.save()
                                messages.success(request,'Cambios guardaos correctamente')
                                return redirect('cliente')
                            else:
                                messages.error(request,'Por favor, Corrige los errores del formulario')
                        else:
                            cliente_form =ClienteForm(instance=cliente)
                        return render(request,'cliente.html',{'cliente': cliente, 'form': cliente_form})
                    except cliente.DoesNotExist:
                        messages.error(request,'No se encontro los datos del cliente')

                else:
                    return redirect('frmempleado')
            form.add_error(None, 'Credenciales invalidas. por favor, intentelo de nuevo')
        return render(request, 'iniciosesion.html',{'form': form})

def frmcliente(request):
     return render(request,"cliente.html")
