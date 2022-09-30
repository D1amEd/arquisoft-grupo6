from ..models import Reporte
import random

def get_reportes():
    reportes = Reporte.objects.all()
    return reportes

def get_reporte(rep_pk):
    reporte = Reporte.objects.get(pk=rep_pk)
    return reporte

def fib(n):
    # base cases
    if n == 0: 
        return 0
    if n == 1: 
        return 1
    
    # recursive step
    return fib(n-1) + fib(n-2)

def update_reporte(rep_pk, new_rep):
    # delay
    n = random.randint(29, 31) # 0.2sec - 0.48sec
    fib(n)
    # update
    reporte = get_reporte(rep_pk)
    reporte.id = new_rep["id"]
    reporte.save()
    return reporte

def create_reporte(rep):
    # delay
    n = random.randint(42, 43) # 92sec (1.5min) - 151sec (2.5min)
    fib(n)
    # creation
    reporte = Reporte(id=rep["id"])
    reporte.save()
    return reporte
