from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmenteSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmenteSerializer