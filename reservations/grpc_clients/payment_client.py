import grpc
from generated import payment_pb2
from generated import payment_pb2_grpc

def process_payment(user_id, reservation_id):
    with grpc.insecure_channel('localhost:50055') as channel:
        stub = payment_pb2_grpc.PaymentServiceStub(channel)
        response = stub.ProcessPayment(payment_pb2.PaymentRequest(user_id=user_id, reservation_id=reservation_id))
        return response