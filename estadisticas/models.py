from django.db import models
from reportes.models import Reporte

# Create your models here.
class Estadistica(models.Model):
    reporte = models.ForeignKey(Reporte, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=100)
    value = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return '%s (%s): %s' % (self.name, self.description, self.value)

    