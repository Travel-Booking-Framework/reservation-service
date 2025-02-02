import grpc
from concurrent import futures
from generated import reservation_pb2
from generated import reservation_pb2_grpc
from .commands import CreateReservationCommand, CancelReservationCommand

class ReservationService(reservation_pb2_grpc.ReservationServiceServicer):
    def CreateReservation(self, request, context):
        command = CreateReservationCommand(request.user_id, request.reservation_type, request.reservation_id)
        reservation = command.execute()
        return reservation_pb2.ReservationResponse(id=reservation.id, status=reservation.status)

    def CancelReservation(self, request, context):
        command = CancelReservationCommand(request.reservation_id)
        reservation = command.execute()
        return reservation_pb2.ReservationResponse(id=reservation.id, status=reservation.status)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    reservation_pb2_grpc.add_ReservationServiceServicer_to_server(ReservationService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()