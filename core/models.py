from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    curso = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.curso}"


class Curso(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    descricao = models.TextField(blank=True, null=True)
    duracao = models.CharField(max_length=50, blank=True, null=True)  # Ex: 4 anos

    def __str__(self):
        return self.nome

