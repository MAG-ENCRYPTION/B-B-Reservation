from django.shortcuts import redirect
from django.urls import path
from . import views

app_name = "reservations"

urlpatterns = [
    path('/reserver', views.reserver, name='reservations'),
    path('/payment/<int:reservation_id>/<int:apartment_id>/', views.payment, name='payment'),
    path('/process-payment/', views.process_payment, name='process_payment'),
    path('/payment-success/', views.payment_success, name='payment_success'),
    path('/payment-cancelled/', views.payment_cancelled, name='payment_cancelled'),
    # path('reserver/', lambda request: redirect('reservations:reserver')),
]
