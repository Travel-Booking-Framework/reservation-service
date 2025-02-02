from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .commands import CreateReservationCommand, CancelReservationCommand
from .serializers import ReservationSerializer

class CreateReservationView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        reservation_type = request.data.get('reservation_type')
        reservation_id = request.data.get('reservation_id')

        command = CreateReservationCommand(user_id, reservation_type, reservation_id)
        reservation = command.execute()

        serializer = ReservationSerializer(reservation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CancelReservationView(APIView):
    def post(self, request, reservation_id):
        command = CancelReservationCommand(reservation_id)
        reservation = command.execute()

        serializer = ReservationSerializer(reservation)
        return Response(serializer.data, status=status.HTTP_200_OK)