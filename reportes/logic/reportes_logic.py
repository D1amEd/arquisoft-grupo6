from ..models import Reporte

def get_reportes():
    reportes = Reporte.objects.all()
    return reportes

def get_reporte(rep_pk):
    reporte = Reporte.objects.get(pk=rep_pk)
    return reporte

def update_reporte(rep_pk, new_rep):
    reporte = get_reporte(rep_pk)
    reporte.id = new_rep["id"]
    reporte.save()
    return reporte

def create_report(rep):
    reporte = Reporte(id=rep["id"])
    reporte.save()
    return reporte