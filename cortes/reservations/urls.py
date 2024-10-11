from django.urls import path
from . import views

urlpatterns = [
    # Vos autres URLs
    path('book-a-table/', views.book_table, name='book-a-table'),
]
