from django.db import models

# Create your models here.
class Appointment(models.Model):
    client_name = models.CharField(max_length=200)
    appointment_datetime = models.DateTimeField()
    staff_name = models.CharField(max_length=200)
    creation_datetime = models.DateTimeField(default="2025-03-22")

    def __str__(self):
        return f"Appointment for {self.client_name} on {self.appoint_datetime} with {self.staff_name}"