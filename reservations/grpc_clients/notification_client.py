import grpc
from generated import notification_pb2
from generated import notification_pb2_grpc

def send_notification(user_id, message):
    with grpc.insecure_channel('localhost:50056') as channel:
        stub = notification_pb2_grpc.NotificationServiceStub(channel)
        response = stub.SendNotification(notification_pb2.NotificationRequest(user_id=user_id, message=message))
        return response