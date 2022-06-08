from django.urls import path
from . import views


urlpatterns = [

    path ("", views.inicio),
    path ("usuarios", views.usuarios, name= 'Usuarios'),
    path ("productos", views.productos, name = 'Productos'),
    path ("autorizaciones", views.autorizaciones, name = 'Autorizaciones'),
    path ("presentaciones", views.presentaciones, name = 'Presentaciones'),
    path ("costos", views.costos, name = 'Costos'),
    path ("alta_usuario", views.usuario_formulario),
    path ("alta_producto", views.producto_formulario),
    path ("alta_costo", views.costo_formulario),
    path ("busqueda_bd", views.buscar_producto),
    path ("buscar", views.buscar),
]