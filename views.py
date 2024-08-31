from rest_framework import generics
from .models import Flight,  Passenger
from .views import FlightSerializer, PassengerSerializer

class FlightListCreateView(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class FlightRetrieveUpdateDestroyView(generics.RetriveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = PassengerSerializer

class PassengerListcreateView(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = PassengerSerializer
class PassengerRetrieveUpdateestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer