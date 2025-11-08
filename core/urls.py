from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # ====== PÁGINA INICIAL ======
    path('', views.HomeView.as_view(), name='home'),

    # ====== NOVIDADES ACADÊMICAS ======
    path('novidades/', views.NovidadesAcademicasView.as_view(), name='novidades'),

    # ====== CRUD ALUNOS ======
    path('alunos/', views.AlunoListView.as_view(), name='aluno_list'),
    path('alunos/novo/', views.AlunoCreateView.as_view(), name='aluno_add'),
    path('alunos/<int:pk>/', views.AlunoDetailView.as_view(), name='aluno_detail'),
    path('alunos/<int:pk>/editar/', views.AlunoUpdateView.as_view(), name='aluno_edit'),
    path('alunos/<int:pk>/deletar/', views.AlunoDeleteView.as_view(), name='aluno_delete'),

    # ====== CRUD CURSOS ======
    path('cursos/', views.CursoListView.as_view(), name='curso_list'),
    path('cursos/novo/', views.CursoCreateView.as_view(), name='curso_create'),
    path('cursos/<int:pk>/editar/', views.CursoUpdateView.as_view(), name='curso_edit'),
    path('cursos/<int:pk>/deletar/', views.CursoDeleteView.as_view(), name='curso_delete'),
]



