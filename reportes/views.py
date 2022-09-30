import json
from django.shortcuts import render
from .logic import reportes_logic as rl
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def reportes_view(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id:
            reporte_dto = rl.get_reporte(id)
            reporte = serializers.serialize('json', [reporte_dto,])
            return HttpResponse(reporte, 'application/json')
        else:
            reportes_dto = rl.get_reportes()
            reportes = serializers.serialize('json', reportes_dto)
            return HttpResponse(reportes, 'application/json')
    if request.method == 'POST':
        reporte_dto = rl.create_reporte(json.loads(request.body))
        reporte = serializers.serialize('json', [reporte_dto,])
        return HttpResponse(reporte, 'application/json')

@csrf_exempt
def reporte_view(request, pk):
    if request.method == 'GET':
        reporte_dto = rl.get_reporte(pk)
        reporte = serializers.serialize('json', [reporte_dto,])
        return HttpResponse(reporte, 'application/json')

    if request.method == 'PUT':
        reporte_dto = rl.update_reporte(pk, json.loads(request.body))
        reporte = serializers.serialize('json', [reporte_dto,])
        return HttpResponse(reporte, 'application/json')
