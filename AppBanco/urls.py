from django.urls import path
from .views import *
from . import views
from .viewsLogin import *
from . import views,viewsLogin


urlpatterns=[
    path('cliente',ListadoClientes.as_view(), name='Clientes'),
    path('insertar/',Insertarcliente.as_view(),name='insertar'),
    path('actualizar/<pk>',Actualizar.as_view(),name='actualizar'),
    path('eliminar/<pk>',Eliminar.as_view(),name='eliminar'),
    path('formularioInsertar',views.formularioInsertar,name='insertar'),

    #registro 
    path('registro/',RegistrasUsuariosView.as_view(),name='iniciar_secion'),
    path('iniciar_sesion/', IniciarSesionView.as_view(), name='iniciar_sesion'),
    path('frmcliente/',viewsLogin.frmcliente, name="frmcliente" ),
    path('frmempleado/',viewsLogin.frmcliente, name="frmempleado" )
    
]

"""path('linea',Listadolineacredito.as_view(), name='Lineas de credito'),
    path('credito',Listadocredito.as_view(), name='Credito'),
    path('usuario',Listadousuarios.as_view(), name='Usuario'),
    path('empleado',Listadoempleado.as_view(), name='Empleado'),"""

