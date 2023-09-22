from django.db import models


class Quotes(models.Model):
    ticketname = models.CharField(max_length=255)
    description = models.CharField(max_length=255)



# Create your models here.
