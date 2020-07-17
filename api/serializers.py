from rest_framework import serializers
from api.models import Usuario, RFID, Temperatura

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')

class RFIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = RFID
        fields = ('__all__')

class TemperaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperatura
        fields = ('__all__')