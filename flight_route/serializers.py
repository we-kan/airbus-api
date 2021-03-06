from rest_framework import serializers

from flight_route.models import FlightRoute, JourneyInfo 

class FlightRouteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FlightRoute
        fields = '__all__'

class JourneyInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JourneyInfo
        fields = '__all__'


