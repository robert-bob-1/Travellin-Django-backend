from django.urls import path

from . import views

urlpatterns = [
    path('', views.getDestinations),
    path('create/', views.postDestination),
    path('update/<int:pk>/', views.updateDestination),
    path('delete/<int:pk>/', views.deleteDestination),
    path('available/', views.getAvailableDestinationsInPeriod),
    path('reservations/', views.getReservations),
    path('reservations/create/', views.postReservation),
    path('reservations/check/', views.checkAvailability),
    path('reservations/<int:pk>/', views.getReservationsForDestination),
]