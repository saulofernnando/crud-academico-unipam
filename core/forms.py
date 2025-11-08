from django import forms
from .models import Aluno, Curso


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'matricula', 'curso', 'email', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número da matrícula'}),
            'curso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Curso do aluno'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail institucional'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(xx) xxxxx-xxxx'}),
        }


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'descricao', 'duracao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do curso'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição do curso', 'rows': 4}),
            'duracao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 4 anos'}),
        }
