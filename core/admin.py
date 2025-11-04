from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'curso', 'email')
    search_fields = ('nome', 'matricula', 'curso', 'email')
