from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from entrega1_app.models import Usuarios, Productos, Costos, Autorizaciones, Presentaciones
from entrega1_app.forms import Usuario_formulario, Producto_formulario, Costo_formulario


# Create your views here.
def inicio (request):
    return render ( request , "inicio.html")

def usuarios (request):
   return render (request, "usuarios.html")

def productos (request):
    return render (request, "productos.html")

def costos (request):
    return render (request, "costos.html")


# Ingreso de una trx autorizada
def autorizaciones (request):
    return render (request, "autorizaciones.html")

# Ingreso de una trx autorizada
def presentaciones (request):
    return render (request, "presentaciones.html")



# Alta del usuario
def usuario_formulario (request):
    if request.method == "POST":

        mi_formulario = Usuario_formulario (request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

       
            usuario = Usuarios (nombre = datos['nombre'], apellido = datos['apellido'], nacimiento = datos['nacimiento'], num_cuenta = datos ['num_cuenta'], fecha_alta = datos ['fecha_alta'])
            usuario.save()
    
            return render (request, "alta_usuario.html")

    return render (request, "alta_usuario.html" )    



# Alta productos
def producto_formulario (request):
    if request.method == "POST":

        mi_formulario = Producto_formulario (request.POST)

        if mi_formulario.is_valid():    
            datos = mi_formulario.cleaned_data

       
            producto = Productos (tipo_prod = datos['tipo_prod'], num_comercio = datos['num_comercio'])
            producto.save()
    
            return render (request, "alta_producto.html")

    return render (request, "alta_producto.html" ) 




# Alta de costos

def costo_formulario (request):
    if request.method == "POST":

        mi_formulario = Costo_formulario (request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

       
            costo = Costos (tipo_costo = datos['tipo_costo'], num_comercio = datos['num_comercio'] )
            costo.save()
    
            return render (request, "alta_costo.html")

    return render (request, "alta_costo.html" ) 


#Busqueda

def buscar_producto (request):
    return render (request, "busqueda_bd.html")

def buscar (request):

    if request.GET['tipo_prod']:
        tipo_prod = request.GET['tipo_prod']
        productos = Productos.objects.filter(tipo_prod__icontains=tipo_prod)
        return render (request, "resultado_busqueda.html", {"productos": productos, "tipo_prod": tipo_prod})

    else:

        return HttpResponse (f"No enviaste datos")