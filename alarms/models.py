from django.db import models

from measurements.models import Measurement

class Alarm(models.Model):
    measurement = models.ManyToManyField(Measurement)
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)
