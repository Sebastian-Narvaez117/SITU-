from django.contrib import admin
from django.urls import path
from appSITUweb.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home'),

    # PASAJEROS 
    path('pasajeros/', pasajeros, name='pasajeros'),
    path('pasajerosEdit/<int:id>', pasajerosEdit, name='pasajerosEdit'),
    path('pasajeros/create/', pasajerosCreate, name='pasajerosCreate'),
    path('eliminar/<int:id>', pasajerosDelete, name='pasajerosDelete'),

    # TARJETAS
    path('tarjetas/', tarjetas, name='tarjetas'),
    path('tarjetas/create/', tarjetasCreate, name='tarjetasCreate'),
    path('tarjetas/edit/<int:id>', tarjetasEdit, name='tarjetasEdit'),
    path('tarjetas/delete/<int:id>', tarjetasDelete, name='tarjetasDelete'),

    # BUSES
    path('buses/', buses, name='buses'),
    path('buses/create/', busesCreate, name='busesCreate'),
    path('buses/edit/<int:id>', busesEdit, name='busesEdit'),
    path('buses/delete/<int:id>', busesDelete, name='busesDelete'),

    # VIAJES
    path('viajes/', viajes, name='viajes'),
    path('viajes/create/', viajesCreate, name='viajesCreate'),
    path('viajes/edit/<int:id>', viajesEdit, name='viajesEdit'),
    path('viajes/delete/<int:id>', viajesDelete, name='viajesDelete'),

    # PAGOS
    path('pagos/', pagos, name='pagos'),
    path('pagos/create/', pagosCreate, name='pagosCreate'),
    path('pagos/edit/<int:id>', pagosEdit, name='pagosEdit'),
    path('pagos/delete/<int:id>', pagosDelete, name='pagosDelete'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)