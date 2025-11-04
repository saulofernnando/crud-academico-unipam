from django.views import generic
from django.urls import reverse_lazy
from .models import Aluno
from .forms import AlunoForm

# Página inicial
class HomeView(generic.TemplateView):
    template_name = 'core/home.html'

# Lista de cursos
class CursosView(generic.TemplateView):
    template_name = 'core/cursos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = [
            "Administração",
            "Agronomia",
            "Análise e Desenvolvimento de Sistemas",
            "Arquitetura e Urbanismo",
            "Biomedicina",
            "Ciências Biológicas",
            "Ciências Contábeis",
            "Comunicação Social - Publicidade e Propaganda",
            "Direito",
            "Educação Física",
            "Enfermagem",
            "Engenharia Civil",
            "Engenharia Elétrica",
            "Engenharia Mecânica",
            "Estética e Cosmética",
            "Farmácia",
            "Fisioterapia",
            "Fonoaudiologia",
            "Gestão Comercial",
            "Gestão de Negócios e Inovação",
            "Gestão de Recursos Humanos",
            "Gestão Financeira",
            "Gestão Pública",
            "História",
            "Logística",
            "Marketing",
            "Mecanização em Agricultura de Precisão",
            "Medicina",
            "Medicina Veterinária",
            "Nutrição",
            "Odontologia",
            "Pedagogia",
            "Psicologia",
            "Sistemas de Informação",
            "Terapia Ocupacional",
        ]
        return context

# Página de Novidades Acadêmicas
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
            {
                "titulo": "Semana do Conhecimento",
                "descricao": "Apresentações de trabalhos científicos e premiação dos melhores projetos interdisciplinares.",
                "data": "10 a 15 de dezembro de 2025"
            },
            {
                "titulo": "Workshop de Inteligência Artificial",
                "descricao": "Aprenda sobre IA aplicada a negócios e tecnologia em um workshop gratuito para alunos.",
                "data": "20 de dezembro de 2025"
            },
        ]
        return context

# CRUD Aluno
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
