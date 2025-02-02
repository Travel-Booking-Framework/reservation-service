from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'user_id', 'reservation_type', 'reservation_id', 'status']
    
    def validate_status(self, value):
        if value not in ['PENDING', 'CONFIRMED', 'CANCELLED']:
            raise serializers.ValidationError("Invalid status")
        return value

    def update_status(self, reservation, status):
        if status == 'CANCELLED':
            reservation.status = 'CANCELLED'
            reservation.save()
        return reservation