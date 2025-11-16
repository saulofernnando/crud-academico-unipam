from django import forms
from .models import Aluno, Curso

class AlunoForm(forms.ModelForm):
    curso_nome = forms.CharField(
        label="Curso",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do curso'})
    )

    class Meta:
        model = Aluno
        fields = ['nome', 'matricula', 'curso_nome', 'email', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número da matrícula'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail institucional'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(xx) xxxxx-xxxx'}),
        }

    def save(self, commit=True):
        nome_curso = self.cleaned_data['curso_nome'].strip()
        curso = Curso.objects.filter(nome__iexact=nome_curso).first()

        if not curso:
            curso = Curso.objects.create(
                nome=nome_curso,
                descricao='',
                duracao='',
                modalidade='Presencial',
                habilitacao=''
            )

        aluno = super().save(commit=False)
        aluno.curso = curso
        if commit:
            aluno.save()
        return aluno


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'habilitacao', 'modalidade', 'duracao', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do curso'}),
            'habilitacao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Bacharelado, Licenciatura...'}),
            'modalidade': forms.Select(attrs={'class': 'form-control'}),
            'duracao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 4 anos'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição do curso', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Deixa a opção em branco no início
        self.fields['modalidade'].choices = [('', 'Selecione uma modalidade')] + list(Curso.MODALIDADE_CHOICES)
