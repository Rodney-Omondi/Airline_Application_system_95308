from django .urls import path
from .serializers import (
    FlightListCreateView,
    FlightRetrieveUpdateDestoyView,
    PassengerListCreateView,
    PassengerRetrieveUpdateDestroyView
)

urlpatterns = [
    path('flights/', FlightListCreateView.as_view(), name='flight-list-create'),
    path('flights/<int:pk>/,FlightRetrieveUpdateDestroyView.as_view(), name='flight-detail'),
    path('passengers/',passengerListCreateView.as_view(), name='passenger-list-create'),
    path('passengers/<int:pk>/',passengerRetrieveUpdateDestroyView.as_view(), name='passenger-detail'),     
]