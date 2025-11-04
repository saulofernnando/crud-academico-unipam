from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('cursos/', views.CursosView.as_view(), name='cursos'),
    path('novidades/', views.NovidadesAcademicasView.as_view(), name='novidades'),
    path('alunos/', views.AlunoListView.as_view(), name='aluno_list'),
    path('alunos/novo/', views.AlunoCreateView.as_view(), name='aluno_add'),
    path('alunos/<int:pk>/', views.AlunoDetailView.as_view(), name='aluno_detail'),
    path('alunos/<int:pk>/editar/', views.AlunoUpdateView.as_view(), name='aluno_edit'),
    path('alunos/<int:pk>/deletar/', views.AlunoDeleteView.as_view(), name='aluno_delete'),
]


