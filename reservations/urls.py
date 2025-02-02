# reservations/urls.py
from django.urls import path
from .views import CreateReservationView, CancelReservationView

urlpatterns = [
    path('reservations/', CreateReservationView.as_view(), name='create-reservation'),
    path('reservations/<int:reservation_id>/cancel/', CancelReservationView.as_view(), name='cancel-reservation'),
]

# Include in main urls.py
from django.urls import include
urlpatterns = [
    path('api/', include('reservations.urls')),
]