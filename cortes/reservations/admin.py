from django.contrib import admin
from .models import TableReservation, MyImage, Apartment, EspaceDeDetente

# Enregistrer les modèles dans l'interface d'administration
admin.site.register(TableReservation)
admin.site.register(MyImage)
admin.site.register(Apartment)
admin.site.register(EspaceDeDetente)
