from django.db import models

class Contato(models.Model):
     nome = models.CharField(max_length=150)
     email = models.EmailField()
     mensagem = models.TextField()

class Reserva(models.Model):
     nome_do_pet = models.CharField(max_length=150)
     telefone = models.CharField(max_length=15)
     data = models.DateField()
     mensagem = models.TextField(blank=True, null=True)