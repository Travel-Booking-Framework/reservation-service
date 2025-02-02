import grpc
from generated import train_pb2
from generated import train_pb2_grpc

class TrainClient:
    def book_train(self, user_id, train_id):
        with grpc.insecure_channel('localhost:50054') as channel:
            stub = train_pb2_grpc.TrainServiceStub(channel)
            response = stub.BookTrain(train_pb2.TrainRequest(user_id=user_id, train_id=train_id))
            return response