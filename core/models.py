# core/models.py
from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    DIA_CHOICES = [
        ('segunda', 'Segunda-feira'),
        ('terca', 'Terça-feira'),
        ('quarta', 'Quarta-feira'),
        ('quinta', 'Quinta-feira'),
        ('sexta', 'Sexta-feira'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
    ]

    dia = models.CharField(max_length=10, choices=DIA_CHOICES)
    tarefa = models.CharField(max_length=255)
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tarefa} ({self.dia})"
