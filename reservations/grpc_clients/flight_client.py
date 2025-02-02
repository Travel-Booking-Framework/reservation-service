import grpc
from generated import flight_pb2
from generated import flight_pb2_grpc

class FlightClient:
    def book_flight(self, user_id, flight_id):
        with grpc.insecure_channel('localhost:50053') as channel:
            stub = flight_pb2_grpc.FlightServiceStub(channel)
            response = stub.BookFlight(flight_pb2.FlightRequest(user_id=user_id, flight_id=flight_id))
            return response