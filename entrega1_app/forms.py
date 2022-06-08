from django import forms 


class Usuario_formulario (forms.Form):

    nombre = forms.CharField (max_length=40)
    apellido = forms.CharField (max_length=40)
    nacimiento = forms.DateField ()
    num_cuenta = forms.IntegerField()
    fecha_alta = forms.DateField ()


class Producto_formulario (forms.Form):

    tipo_prod = forms.CharField (max_length=40)
    num_comercio = forms.IntegerField()
 

class Costo_formulario (forms.Form):

    tipo_costo = forms.CharField (max_length=40)
    num_comercio = forms.IntegerField()



