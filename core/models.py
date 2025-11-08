from django.db import models

class Curso(models.Model):
    MODALIDADE_CHOICES = [
        ('Presencial', 'Presencial'),
        ('EAD', 'Educação a Distância'),
        ('Híbrido', 'Híbrido'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    duracao = models.CharField(max_length=50, blank=True, null=True)
    modalidade = models.CharField(
        max_length=50,
        choices=MODALIDADE_CHOICES,
        default='Presencial',
        help_text='Selecione a modalidade do curso'
    )
    habilitacao = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text='Ex: Bacharelado, Licenciatura, Tecnólogo'
    )

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.curso.nome}"


