from django.db import models

class Ticket(models.Model):

    question = models.CharField(max_length=500, blank=False)
    admin_response = models.CharField(max_length=500, blank=True)
    accepted = models.BooleanField(default=False)
