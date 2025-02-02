from pybreaker import CircuitBreaker
from .repositories import ReservationRepository
from .grpc_clients import HotelClient, FlightClient, TrainClient, PaymentClient, NotificationClient

hotel_client = HotelClient()
flight_client = FlightClient()
train_client = TrainClient()
payment_client = PaymentClient()
notification_client = NotificationClient()

# CircuitBreaker Pattern
reservation_breaker = CircuitBreaker(fail_max=3, reset_timeout=60)

class CreateReservationCommand:
    def __init__(self, user_id, reservation_type, reservation_id):
        self.user_id = user_id
        self.reservation_type = reservation_type
        self.reservation_id = reservation_id

        # Mapping reservation types to client methods
        self.reservation_clients = {
            'HOTEL': hotel_client.book_hotel,
            'FLIGHT': flight_client.book_flight,
            'TRAIN': train_client.book_train
        }

    @reservation_breaker
    def execute(self):
        reservation = ReservationRepository.create_reservation(
            self.user_id, self.reservation_type, self.reservation_id
        )

        # Strategy Pattern
        if self.reservation_type in self.reservation_clients:
            self.reservation_clients[self.reservation_type](self.user_id, self.reservation_id)
        else:
            raise ValueError(f"Unsupported reservation type: {self.reservation_type}")

        payment_client.process_payment(self.user_id, self.reservation_id)

        notification_client.send_notification(self.user_id, f"Reservation {self.reservation_id} created.")

        return reservation

class CancelReservationCommand:
    def __init__(self, reservation_id):
        self.reservation_id = reservation_id

    @reservation_breaker
    def execute(self):
        reservation = ReservationRepository.cancel_reservation(self.reservation_id)

        notification_client.send_notification(reservation.user_id, f"Reservation {self.reservation_id} cancelled.")

        return reservation
