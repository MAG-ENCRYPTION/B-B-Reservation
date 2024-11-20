from django.db import models


class TableReservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    people = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name


class MyImage(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    local = models.CharField(max_length=200, blank=True, null=True)  # Nouveau champ

    def __str__(self):
        return self.name

from django.db import models
class Apartment(models.Model):
    name = models.CharField(max_length=100)  # Nom de l'appartement
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)  # Prix par nuit
    description = models.TextField()  # Description de l'appartement
    image = models.ForeignKey(MyImage, on_delete=models.CASCADE, related_name='apartments')  # Image principale
    category = models.CharField(max_length=50, choices=[
        ('one-bedroom', 'One Bedroom'),
        ('two-bedroom', 'Two Bedroom'),
        ('studio', 'Studio'),
        ('special', 'Special'),
    ])  # Catégorie de l'appartement


    def __str__(self):
        return f"{self.name} - ${self.price_per_night}/nuit"


class EspaceDeDetente(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ForeignKey(MyImage, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.titre
    

