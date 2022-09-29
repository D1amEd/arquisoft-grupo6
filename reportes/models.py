from django.db import models

# Create your models here.
class Reporte(models.Model):
    id = models.IntegerField(primary_key=True)    
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s\n%s' % (self.id, self.fecha)
