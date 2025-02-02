import grpc
from generated import hotel_pb2
from generated import hotel_pb2_grpc

def book_hotel(user_id, hotel_id):
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = hotel_pb2_grpc.HotelServiceStub(channel)
        response = stub.BookHotel(hotel_pb2.HotelRequest(user_id=user_id, hotel_id=hotel_id))
        return response