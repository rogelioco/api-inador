from django.db import models
from django.utils import timezone
# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length = 50, null = False)
    apellido = models.CharField(max_length = 50, null = False)
    fecha_nacimiento = models.DateField(null = False)
    rol = models.CharField(max_length = 50, null = False)
    create = models.DateField(default = timezone.now)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Usuario'

class RFID(models.Model):
    key = models.CharField(max_length = 150, null = False)
    id_usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    create = models.DateField(default = timezone.now)

    def __str__(self):
        return self.key

    class Meta :
        db_table = 'RFID'

class Temperatura(models.Model):
    temperatura = models.CharField(max_length = 50, null = False)
    id_rfid = models.ForeignKey(RFID, on_delete = models.CASCADE)
    create = models.DateField(default = timezone.now)

    def __str__(self):
        return self.temperatura
    class Meta:
        db_table = 'Temperatura'
