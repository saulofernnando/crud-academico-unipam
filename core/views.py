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
                "data": "10 a 14 de novembro de 2025",
                "link": "#"
            },
            {
                "titulo": "Novo Laboratório de Inovação Aberto",
                "descricao": "Laboratório com impressoras 3D, robótica e prototipagem já está em funcionamento.",
                "data": "20 de novembro de 2025",
                "link": "#"
            },
            {
                "titulo": "Inscrições para o Vestibular 2026",
                "descricao": "As inscrições para novos cursos de graduação já estão abertas.",
                "data": "30 de novembro de 2025",
                "link": "#"
            },
            {
                "titulo": "Biblioteca Ganha 200 Novos Livros",
                "descricao": "A biblioteca do UNIPAM recebeu uma grande atualização no acervo acadêmico.",
                "data": "05 de dezembro de 2025",
                "link": "#"
            },
            {
                "titulo": "Novo Curso de Ciência de Dados",
                "descricao": "O curso começa em 2026 e inclui disciplinas de IA, big data e machine learning.",
                "data": "12 de dezembro de 2025",
                "link": "#"
            },
            {
                "titulo": "Expansão do Estacionamento",
                "descricao": "As obras do novo estacionamento do campus foram iniciadas.",
                "data": "18 de dezembro de 2025",
                "link": "#"
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
    success_url = reverse_lazy('core:curso_list')


class CursoCreateView(generic.CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'core/curso_form.html'
    success_url = reverse_lazy('core:curso_list')

    def form_valid(self, form):
        print("📘 Dados enviados:", form.cleaned_data)
        return super().form_valid(form)
