from rest_framework import serializers
from .models import Appointment

class AppointmenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'client_name', 'appointment_datetime', 'staff_name']
        