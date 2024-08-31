from rest_framework import serializers
from .models import Flight, Passenger

class Flightserializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
class PassengerSerializer(serializers.Modelserializer):
    class Meta:
        model = Passenger
        fields = '__all__'


