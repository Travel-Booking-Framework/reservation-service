from pybreaker import CircuitBreaker
from .repositories import ReservationRepository

reservation_breaker = CircuitBreaker(fail_max=3, reset_timeout=60)

class CreateReservationCommand:
    def __init__(self, user_id, reservation_type, reservation_id):
        self.user_id = user_id
        self.reservation_type = reservation_type
        self.reservation_id = reservation_id

    @reservation_breaker
    def execute(self):
        return ReservationRepository.create_reservation(
            self.user_id, self.reservation_type, self.reservation_id
        )

class CancelReservationCommand:
    def __init__(self, reservation_id):
        self.reservation_id = reservation_id

    @reservation_breaker
    def execute(self):
        return ReservationRepository.cancel_reservation(self.reservation_id)