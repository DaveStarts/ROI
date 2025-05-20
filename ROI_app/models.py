from django.db import models

# Create your models here.

class Programm(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Kalkulation(models.Model):
    kalk_ID = models.AutoField(primary_key=True)
    programm = models.ForeignKey(Programm, related_name='kalk_ids', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Projekt(models.Model):
    projekt_ID = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name
    
class Variante(models.Model):
    Variante_ID = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name
    
class Varianten_Daten(models.Model):
    Varianten_Daten_ID = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name
    
class Investition(models.Model):
    Investition_ID = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

class Investition_Daten(models.Model):
    Investition_Daten_ID = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name