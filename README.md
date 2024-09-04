# Agenda Semanal

Descrição do Projeto -
A Agenda Semanal é uma aplicação web desenvolvida em Django que permite aos usuários organizar suas tarefas semanais de forma eficiente. Cada dia da semana possui uma tabela separada onde o usuário pode adicionar, editar e excluir tarefas, especificando o horário de início e término para cada atividade. A aplicação é ideal para aqueles que buscam uma maneira simples e intuitiva de gerenciar suas tarefas diárias.

Funcionalidades -
Cadastro de Usuários: Sistema de autenticação que permite que cada usuário tenha sua própria agenda.
Gerenciamento de Tarefas: Adicione, edite e exclua tarefas para cada dia da semana.
Visualização da Agenda: Veja todas as suas tarefas organizadas por dia da semana.
Responsividade: Interface responsiva que se adapta a diferentes tamanhos de tela.

Backend -
Django: Framework web utilizado para desenvolver o backend da aplicação, gerenciar rotas, autenticação, e interações com o banco de dados.
Python: Linguagem de programação usada para toda a lógica de negócios e manipulação de dados.

Frontend -
HTML/CSS: Utilizados para estruturar e estilizar as páginas.
Bootstrap: Framework CSS utilizado para garantir a responsividade e melhorar o design da interface.

Banco de Dados -
SQLite3: Banco de dados relacional leve, utilizado para armazenar todas as informações do sistema, como usuários e suas respectivas tarefas. Cada tabela no banco de dados representa um dia da semana, com colunas para a descrição da tarefa, horário de início e horário de término.

Estrutura do Projeto -
manage.py: Script de gerenciamento do Django.
settings.py: Configurações do Django, incluindo configurações de banco de dados e aplicativos instalados.
urls.py: Configuração de URLs que mapeia as rotas do projeto.
models.py: Modelos de dados que definem a estrutura das tabelas no banco de dados.
views.py: Funções de visualização que manipulam as requisições e retornam as respostas para os templates.
templates/: Diretório contendo os arquivos HTML que renderizam as páginas do usuário.

## Instalação

1. Clone o repositório:
   ```bash
git clone https://github.com/renanjatczak/agenda_semanal

# Navegue até o diretório do projeto:
cd agenda_semanal

# Crie e ative um ambiente virtual:
python -m venv ambientevirtual
# No Windows:
ambientevirtual\Scripts\activate
# No macOS/Linux:
source ambientevirtual/bin/activate

# Instale as dependências:
pip install -r requirements.txt

# Execute as migrações:
python manage.py migrate

# (Opcional) Crie um superusuário:
python manage.py createsuperuser

# Execute o servidor de desenvolvimento:
python manage.py runserver
