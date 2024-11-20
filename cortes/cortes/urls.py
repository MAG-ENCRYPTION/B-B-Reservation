from django.contrib import admin
from django.urls import path
from reservations import views  # Import des vues de l'application reservations

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Vue principale

    # Routes liées à l'application reservations
    path('reserver/', views.reserver, name='reserver'),
    path('payment/<int:reservation_id>/<int:apartment_id>/', views.payment, name='payment'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('payment-cancelled/', views.payment_cancelled, name='payment_cancelled'),
]
