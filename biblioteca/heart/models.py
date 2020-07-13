from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


class Editora(models.Model):
    Id_Ed = models.CharField(max_length=100)
    Nome = models.CharField(max_length=50)
    Edereco = models.CharField(max_length=100)
    Telefone = models.CharField(max_length=14)
    Site = models.CharField(max_length=100)

    def __str__(self):
        return self.Nome


class Livro(models.Model):
    Id_Li = models.CharField(max_length=100)
    Nome = models.CharField(max_length=100)
    Autor = models.CharField(max_length=100)
    Resumo = models.TextField()
    Observacao = models.CharField(max_length=100)
    Imag = models.ImageField(upload_to='capas')
    Editora = models.ForeignKey(Editora, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nome


class Reservar(models.Model):
    Nome = models.ForeignKey(User, on_delete=models.CASCADE)
    Nome_liv = models.ForeignKey(Livro, on_delete=models.CASCADE)
    Devolver = models.DateField()

    def __str__(self):
        return str(self.Nome_liv)


class Reporter(models.Model):
    full_name = models.CharField(max_length=70)
    email = models.EmailField()
    active = models.BooleanField(True)
    senha = models.CharField(max_length=5)

    def __str__(self):
        return self.full_name
# Create your models here.
