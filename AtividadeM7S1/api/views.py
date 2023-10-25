from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Reserva, Contato

@api_view()
def reservas(request):
     consulta = Reserva.objects.all()
     dados = []
     for reserva in consulta:
          dado = {
               "id": reserva.id,
               "nome_do_pet" : reserva.nome_do_pet,
               "telefone" : reserva.telefone,
               "data" : reserva.data,
               "mensagem" : reserva.mensagem
          }
          dados.append(dado)

     return Response(dados)

@api_view()
def contatos(request):
     consulta = Contato.objects.all()
     dados = []
     for contato in consulta:
          dado = {
               "id": contato.id,
               "nome" : contato.nome,
               "email" : contato.email,
               "mensagem" : contato.mensagem,
          }
          dados.append(dado)

     return Response(dados)