from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import UsuarioSerializer, RFIDSerializer, TemperaturaSerializer
from api.models import Usuario, RFID, Temperatura
#-----------------------------------CRUD Usuario----------------------------------
@api_view(['GET'])
def apiOverview (request):
    api_urls = {
        'hola',
        'bb',
        'como',
        'tas',
    }
    return Response(api_urls)
    
@api_view(['GET'])
def usuarioShow(request):
    usuario = Usuario.objects.all()
    serializer = UsuarioSerializer(usuario, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def usuarioCreate(request):
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def usuarioRead(request, pk):
    usuario = Usuario.objects.get(id=pk)
    serializer = UsuarioSerializer(usuario, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def usuarioUpdate(request, pk):
    usuario = Usuario.objects.get(id=pk)

    serializer = UsuarioSerializer(instance=usuario, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def usuarioDelete(request, pk):
    usuario = Usuario.objects.get(id=pk)
    usuario.delete()

    return Response('Usuario eliminado :]')

#----------------------------------CRUD RFID----------------------------------
    
@api_view(['GET'])
def rfidShow(request):
    rfid = RFID.objects.all()
    serializer = RFIDSerializer(rfid, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def rfidCreate(request):
    serializer = RFIDSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def rfidRead(request, pk):
    rfid = RFID.objects.get(id=pk)
    serializer = RFIDSerializer(rfid, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def rfidUpdate(request, pk):
    rfid = RFID.objects.get(id=pk)

    serializer = RFIDSerializer(instance=rfid, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def rfidDelete(request, pk):
    rfid = RFID.objects.get(id=pk)
    rfid.delete()

    return Response('Usuario eliminado :]')

#---------------------------------------CRUD Temperatura----------------------------

@api_view(['GET'])
def tempShow(request):
    temperatura = Temperatura.objects.all()
    serializer = TemperaturaSerializer(temperatura, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def tempCreate(request):
    serializer = TemperaturaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def tempRead(request, pk):
    temperatura = Temperatura.objects.get(id=pk)
    serializer = TemperaturaSerializer(temperatura, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def tempUpdate(request, pk):
    temperatura = Temperatura.objects.get(id=pk)

    serializer = TemperaturaSerializer(instance=temperatura, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def tempDelete(request, pk):
    temperatura = Temperatura.objects.get(id=pk)
    temperatura.delete()

    return Response('Temperatura eliminado :]')