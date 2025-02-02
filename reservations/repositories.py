from .models import Reservation

# Repository Pattern
class ReservationRepository:
    @staticmethod
    def create_reservation(user_id, reservation_type, reservation_id):
        return Reservation.objects.create(
            user_id=user_id,
            reservation_type=reservation_type,
            reservation_id=reservation_id,
        )

    @staticmethod
    def cancel_reservation(reservation_id):
        reservation = Reservation.objects.get(id=reservation_id)
        reservation.status = 'CANCELLED'
        reservation.save()
        return reservation