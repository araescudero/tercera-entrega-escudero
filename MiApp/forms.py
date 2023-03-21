from django import forms
from MiApp.models import Compra, Proveedor, Servicio

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'