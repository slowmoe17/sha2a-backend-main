from django.urls import path
from .views import (
    ListShuttle,
    CreateShuttleReservation,
    DriverShuttlesRequests,
)

urlpatterns = [
    path('', ListShuttle.as_view()),
    path('book/', CreateShuttleReservation.as_view()),
    path('driver/', DriverShuttlesRequests.as_view()),

]