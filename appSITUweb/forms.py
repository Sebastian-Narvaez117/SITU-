from django import forms
from .models import Pasajero, Tarjeta, Bus, Viaje, SimularAccesoPago

class PasajeroFormulario(forms.ModelForm):
	class Meta:
		model = Pasajero
		fields=["cedula","nombre","apellido", "email","imagen","telefono"] 
        
		#fields = '__all__'

class TarjetaFormulario(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = '__all__'
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'monto': forms.TextInput(attrs={'class': 'form-control'}),
            'idPasajero': forms.Select(attrs={'class': 'form-control'}),
        }
class BusFormulario(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ["placa","cooperativa","numero"]
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'cooperativa': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ViajeFormulario(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = '__all__'
        widgets = {
            'pasajero': forms.Select(attrs={'class': 'form-control'}),
            'bus': forms.Select(attrs={'class': 'form-control'}),
            'costo': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'efectivo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
        }                		
class SimularAccesoPagoFormulario(forms.ModelForm):
    class Meta:
        model = SimularAccesoPago
        fields = '__all__'
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'viaje': forms.Select(attrs={'class': 'form-control'}),
            'tarjeta': forms.Select(attrs={'class': 'form-control'}),
        }        