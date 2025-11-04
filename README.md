# Portal Acadêmico - CRUD Demo (Django)

Projeto de exemplo para atender à atividade: CRUD (Inserir, Visualizar, Atualizar e Excluir) com pelo menos 5 campos.
Aplicação simples para gerenciar registros de **Aluno**.

## Requisitos
- Python 3.10+ (recomendado)
- pip
- (Opcional) virtualenv ou venv

## Instalação e execução (passo a passo)
1. Abra um terminal (PowerShell no Windows).
2. Vá para a pasta onde descompactou o projeto. Ex: `cd C:\Users\SeuUsuario\Downloads\portal_academico_demo`
3. Crie e ative um ambiente virtual (opcional, recomendado):
   - Windows (PowerShell): `python -m venv venv` e depois `venv\Scripts\Activate.ps1`
   - Windows (cmd): `python -m venv venv` e depois `venv\Scripts\activate.bat`
   - Linux/macOS: `python3 -m venv venv` e depois `source venv/bin/activate`
4. Instale dependências:
   ```
   pip install -r requirements.txt
   ```
5. Execute migrações para criar o banco (SQLite por padrão):
   ```
   python manage.py migrate
   ```
6. (Opcional) Crie um superusuário para acessar o admin:
   ```
   python manage.py createsuperuser
   ```
7. Execute o servidor de desenvolvimento:
   ```
   python manage.py runserver
   ```
8. Acesse no navegador: `http://127.0.0.1:8000/` e vá para `/alunos/` para ver o CRUD.

## Banco de dados
- O projeto usa **SQLite** por padrão (arquivo `db.sqlite3` no diretório do projeto).
- Para alterar para outro SGBD (Postgres, MySQL), edite `portal_academico/settings.py` na variável `DATABASES` e instale o driver correspondente (psycopg2 para Postgres, mysqlclient para MySQL).

## Onde alterar os códigos (principais arquivos)
- `portal_academico/settings.py`: configurações do projeto (DEBUG, DB, static, SECRET_KEY).
- `core/models.py`: defina os modelos (aqui está `Aluno` com 5 campos).
- `core/forms.py`: formulários (ModelForm utilizado para criar/editar).
- `core/views.py`: views/controle do CRUD.
- `core/urls.py`: rotas relacionadas ao app.
- `templates/`: todos os templates HTML das páginas.
- `static/`: css/arquivos estáticos.
- `manage.py`: utilitário para comandos Django.

## Observações sobre erros comuns e como resolver
- **'django' not found**: instale dependências (`pip install -r requirements.txt`).
- **Erros de import**: verifique se você está na pasta raiz contendo `manage.py` antes de rodar `python manage.py runserver`.
- **Permissões/Lock de arquivo no Windows**: feche programas que possam estar usando o arquivo `db.sqlite3`.
- **Pastas com espaços ou caracteres especiais**: evite caminhos com acentuação ou caracteres especiais para evitar problemas no Windows.
- **Se quiser enviar ao GitHub**:
  ```bash
  git init
  git add .
  git commit -m "Projeto CRUD Django - demo"
  # crie repositório no GitHub e então:
  git remote add origin https://github.com/SEU_USUARIO/REPO.git
  git push -u origin main
  ```


