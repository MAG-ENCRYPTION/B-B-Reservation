from django.shortcuts import render, redirect
from .forms import TableReservationForm
from django.db.models import Sum
from django.contrib import messages
from .models import TableReservation
from django.core.mail import send_mail
from datetime import time


import logging

logger = logging.getLogger(__name__)


def index(request):

    gallery_images = [
        {'url': 'img/gallery/gallery-1.jpg', 'alt': 'Appartement 1'},
        {'url': 'img/gallery/gallery-2.jpg', 'alt': 'Appartement 2'},
        {'url': 'img/gallery/gallery-3.jpg', 'alt': 'Appartement 3'},
        {'url': 'img/gallery/gallery-4.jpg', 'alt': 'Appartement 4'},
        {'url': 'img/gallery/gallery-5.jpg', 'alt': 'Appartement 5'},
        {'url': 'img/gallery/gallery-6.jpg', 'alt': 'Appartement 6'},
        {'url': 'img/gallery/gallery-7.jpg', 'alt': 'Appartement 7'},
        {'url': 'img/gallery/gallery-8.jpg', 'alt': 'Appartement 8'},
    ]
    chefs = [
        {
            'name': 'Alice Dubois',
            'position': 'Directrice Générale',
            'photo': 'img/chefs/chef-1.jpg',
            'social_links': {
                'twitter': '#',
                'facebook': '#',
                'instagram': '#',
                'linkedin': '#',
            }
        },
        {
            'name': 'Jean Dupont',
            'position': 'Directeur des Opérations',
            'photo': 'img/chefs/chef-2.jpg',
            'social_links': {
                'twitter': '#',
                'facebook': '#',
                'instagram': '#',
                'linkedin': '#',
            }
        },
        {
            'name': 'Claire Martin',
            'position': 'Responsable Marketing',
            'photo': 'img/chefs/chef-3.jpg',
            'social_links': {
                'twitter': '#',
                'facebook': '#',
                'instagram': '#',
                'linkedin': '#',
            }
        },
        {
            'name': 'Marc Lefevre',
            'position': 'Directeur Financier',
            'photo': 'img/chefs/chef-4.jpg',
            'social_links': {
                'twitter': '#',
                'facebook': '#',
                'instagram': '#',
                'linkedin': '#',
            }
        },
    ]

    return render(request, 'index.html', {'gallery_images': gallery_images, 'chefs': chefs})


def book_table(request):
    MAX_PEOPLE_PER_TABLE = 20  # Limite maximale par table
    MAX_PEOPLE = 50  # Nombre maximal de personnes
    form = TableReservationForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        reservation_date = form.cleaned_data['date']
        reservation_time = form.cleaned_data['time']
        reservation_people = form.cleaned_data['people']
        reservation_message = form.cleaned_data['message']

        # Initialiser total_people à 0
        total_people = 0

        # Vérifier d'abord si le nombre de personnes dépasse la limite par table
        if reservation_people > MAX_PEOPLE_PER_TABLE:
            messages.error(request, 'Sorry, we cannot accommodate your party as it exceeds our per table limit.')
            return render(request, 'index.html', {'form': form})

        # Définir les créneaux horaires
        evening_start, evening_end = time(18, 0), time(22, 0)
        lunch_start, lunch_end = time(11, 30), time(14, 30)

        # Vérifier si la réservation est hors des créneaux horaires autorisés
        if not (lunch_start <= reservation_time < lunch_end or evening_start <= reservation_time < evening_end):
            messages.error(request, "Sorry, we cannot accommodate your reservation as it is outside our "
                                    "service hours.")
            return render(request, 'index.html', {'form': form})

        # Vérifier si la réservation est dans l'un des créneaux
        if lunch_start <= reservation_time < lunch_end or evening_start <= reservation_time < evening_end:
            # Calculer le total des personnes pour le créneau concerné
            total_people = TableReservation.objects.filter(
                date=reservation_date,
                time__gte=lunch_start if reservation_time < lunch_end else evening_start,
                time__lt=lunch_end if reservation_time < lunch_end else evening_end,
            ).aggregate(sum=Sum('people'))['sum'] or 0

            total_people += form.cleaned_data['people']

        if total_people <= MAX_PEOPLE:
            reservation = form.save()
            messages.success(request, 'Your reservation has been successfully made.')

            # Envoyer un e-mail de confirmation au client
            send_mail(
                'Confirmation de Réservation',
                f'Votre réservation pour le {reservation.date} à {reservation.time} au nombre de'
                f' {reservation_people} a été confirmée.',
                'michael.benoit13@gmail.com',  # Remplacez par votre adresse e-mail d'envoi
                [reservation.email],  # E-mail du client
                fail_silently=False,
            )

            # Envoyer un e-mail de notification au restaurant
            send_mail(
                'Nouvelle Réservation',
                f'Une nouvelle réservation a été effectuée pour le {reservation.date} à {reservation.time} de '
                f'{reservation_people} personnes, attention voici le message du client : {reservation_message}.',
                'michael.benoit13@gmail.com',  # Remplacez par votre adresse e-mail d'envoi
                ['michael.benoit13@gmail.com'],  # Remplacez par l'e-mail du restaurant
                fail_silently=False,
            )

        else:
            messages.error(request, 'Sorry, we cannot accommodate your party as it exceeds our capacity limit.')

            # Envoyer un e-mail de non-disponibilité au client
            send_mail(
                'Réservation Non Disponible',
                'Nous sommes désolés, '
                'mais nous ne pouvons pas accueillir votre réservation '
                'à la date et à lheure choisies.', 'michael.benoit13@gmail.com',
                [form.cleaned_data['email']],  # E-mail du client
                fail_silently=False,
            )

        return redirect('index')

    return render(request, 'index.html', {'form': form})
