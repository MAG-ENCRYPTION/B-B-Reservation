# PFResto : Système de Réservation pour Restaurant

## Description

Ce projet vise à développer une application web de gestion des réservations pour un restaurant. 
Il s'agit d'une solution conçue pour optimiser la gestion des flux de clients et améliorer la communication entre le restaurant et ses clients. 
L'application permet de gérer les réservations, d'envoyer des confirmations et des rappels par email, et de respecter les contraintes spécifiques du restaurant, telles que la capacité maximale et la taille limite des tables.

## Fonctionnalités

Gestion des Réservations : Permet aux clients de réserver une table en ligne et au personnel du restaurant de gérer ces réservations.
Confirmation et Rappels par Email : Envoie automatiquement des confirmations de réservation et des rappels aux clients et au restaurant.
Respect des Contraintes du Restaurant : Gère la capacité maximale de 50 personnes et les réservations de table jusqu'à 20 personnes.
Gestion des Créneaux Horaires : Permet de gérer les réservations en fonction des créneaux horaires disponibles.

## Technologies Utilisées

Backend : Python 3.10.7, Django 4.2.7.

Frontend : HTML,CSS, JS : Restaurantly - Restaurant Website Template

Base de Données : postgreSQL

Système de Mailing : 

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER =   # Votre adresse mail

EMAIL_HOST_PASSWORD =   # Votre mot de passe mail

## Installation

pip install -r requirements.txt

python manage.py runserver

## Crédits

Le template peut être trouvé à https://bootstrapmade.com/restaurantly-restaurant-template/
