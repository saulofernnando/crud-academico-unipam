from django.views import generic
from django.urls import reverse_lazy
from .models import Aluno, Curso
from .forms import AlunoForm, CursoForm

# ===== PÁGINA INICIAL =====
class HomeView(generic.TemplateView):
    template_name = 'core/home.html'


# ===== PÁGINA DE NOVIDADES =====
class NovidadesAcademicasView(generic.TemplateView):
    template_name = 'core/novidades.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['novidades'] = [
            {
                "titulo": "Semana de Tecnologia 2025",
                "descricao": "Evento anual com palestras sobre IA, segurança cibernética e desenvolvimento web.",
                "data": "10 a 14 de novembro de 2025"
            },
            {
                "titulo": "Novo Laboratório de Inovação Aberto",
                "descricao": "O UNIPAM inaugurou o novo espaço de inovação com impressoras 3D e laboratórios de prototipagem.",
                "data": "20 de novembro de 2025"
            },
            {
                "titulo": "Inscrições para o Vestibular 2026",
                "descricao": "As inscrições estão abertas para os cursos de graduação. Garanta sua vaga!",
                "data": "30 de novembro de 2025"
            },
        ]
        return context


# ===== CRUD ALUNOS =====
class AlunoListView(generic.ListView):
    model = Aluno
    template_name = 'core/aluno_list.html'
    context_object_name = 'alunos'
    paginate_by = 10
    queryset = Aluno.objects.all().order_by('nome')


class AlunoCreateView(generic.CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'core/aluno_form.html'
    success_url = reverse_lazy('core:aluno_list')


class AlunoDetailView(generic.DetailView):
    model = Aluno
    template_name = 'core/aluno_detail.html'
    context_object_name = 'aluno'


class AlunoUpdateView(generic.UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'core/aluno_form.html'
    success_url = reverse_lazy('core:aluno_list')


class AlunoDeleteView(generic.DeleteView):
    model = Aluno
    template_name = 'core/aluno_confirm_delete.html'
    success_url = reverse_lazy('core:aluno_list')


# ===== CRUD CURSOS =====
class CursoListView(generic.ListView):
    model = Curso
    template_name = 'core/curso_list.html'
    context_object_name = 'cursos'
    paginate_by = 10
    queryset = Curso.objects.all().order_by('nome')


class CursoCreateView(generic.CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'core/curso_form.html'
    success_url = reverse_lazy('core:curso_list')


class CursoUpdateView(generic.UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'core/curso_form.html'
    success_url = reverse_lazy('core:curso_list')


class CursoDeleteView(generic.DeleteView):
    model = Curso
    template_name = 'core/curso_confirm_delete.html'
    success_url = reverse_lazy('core:curso_list')  # Redireciona para a página de gerenciamento de cursos
