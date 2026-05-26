from django.shortcuts import render, redirect, get_object_or_404
from .models import Pasajero,Tarjeta, Bus, Viaje, SimularAccesoPago
from .forms import PasajeroFormulario,TarjetaFormulario, BusFormulario, ViajeFormulario, SimularAccesoPagoFormulario


def home_view(request):
    return render(request, "index.html")



def pasajeros(request):
    pasajeros = Pasajero.objects.all()

    if request.method == 'POST':
        formulario = PasajeroFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('pasajeros')  

    else:
        formulario = PasajeroFormulario()

    return render(request, "pasajeros.html", {
        "pasajeros": pasajeros,
        "form": formulario
    })
def pasajerosCreate(request):
    if request.method == 'POST':
        form = PasajeroFormulario(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('pasajeros')
    else:
        form = PasajeroFormulario()  

    return render(request, 'form.html', {'form': form})

def pasajerosEdit(request, id):
    pasajero = get_object_or_404(Pasajero, id=id)

    if request.method == 'POST':
        formulario = PasajeroFormulario(request.POST, request.FILES, instance=pasajero)
        if formulario.is_valid():
            formulario.save()
            return redirect("pasajeros")
    else:
        formulario = PasajeroFormulario(instance=pasajero)

    return render(request, 'pasajerosEdit.html', {
        'form': formulario
    })



def pasajerosDelete(request, id):
    pasajero = get_object_or_404(Pasajero, id=id)
    pasajero.delete()
    return redirect("pasajeros")
# =========================
# TARJETAS
# =========================

def tarjetas(request):
    lista = Tarjeta.objects.all()
    return render(request, 'tarjetas.html', {'tarjetas': lista})

def tarjetasCreate(request):
    if request.method == 'POST':
        form = TarjetaFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarjetas')
    else:
        form = TarjetaFormulario()
    return render(request, 'form.html', {'form': form})

def tarjetasEdit(request, id):
    obj = get_object_or_404(Tarjeta, id=id)

    if request.method == 'POST':
        form = TarjetaFormulario(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('tarjetas')
    else:
        form = TarjetaFormulario(instance=obj)

    return render(request, 'form.html', {'form': form})

def tarjetasDelete(request, id):
    obj = get_object_or_404(Tarjeta, id=id)
    obj.delete()
    return redirect('tarjetas')


# =========================
# BUSES


def buses(request):
    lista = Bus.objects.all()
    return render(request, 'buses.html', {'buses': lista})

def busesCreate(request):
    if request.method == 'POST':
        form = BusFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buses')
    else:
        form = BusFormulario()
    return render(request, 'form.html', {'form': form})

def busesEdit(request, id):
    obj = get_object_or_404(Bus, id=id)

    if request.method == 'POST':
        form = BusFormulario(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('buses')
    else:
        form = BusFormulario(instance=obj)

    return render(request, 'form.html', {'form': form})

def busesDelete(request, id):
    obj = get_object_or_404(Bus, id=id)
    obj.delete()
    return redirect('buses')


# =========================
# VIAJES


def viajes(request):
    lista = Viaje.objects.all()
    return render(request, 'viajes.html', {'viajes': lista})

def viajesCreate(request):
    if request.method == 'POST':
        form = ViajeFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viajes')
    else:
        form = ViajeFormulario()
    return render(request, 'form.html', {'form': form})

def viajesEdit(request, id):
    obj = get_object_or_404(Viaje, id=id)

    if request.method == 'POST':
        form = ViajeFormulario(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('viajes')
    else:
        form = ViajeFormulario(instance=obj)

    return render(request, 'form.html', {'form': form})

def viajesDelete(request, id):
    obj = get_object_or_404(Viaje, id=id)
    obj.delete()
    return redirect('viajes')


# =========================
# PAGOS


def pagos(request):
    lista = SimularAccesoPago.objects.all()
    return render(request, 'pagos.html', {'pagos': lista})

def pagosCreate(request):
    if request.method == 'POST':
        form = SimularAccesoPagoFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagos')
    else:
        form = SimularAccesoPagoFormulario()
    return render(request, 'form.html', {'form': form})

def pagosEdit(request, id):
    obj = get_object_or_404(SimularAccesoPago, id=id)

    if request.method == 'POST':
        form = SimularAccesoPagoFormulario(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('pagos')
    else:
        form = SimularAccesoPagoFormulario(instance=obj)

    return render(request, 'form.html', {'form': form})

def pagosDelete(request, id):
    obj = get_object_or_404(SimularAccesoPago, id=id)
    obj.delete()
    return redirect('pagos')