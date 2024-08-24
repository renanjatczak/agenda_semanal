# Agenda Semanal

Este projeto é uma aplicação Django para gerenciamento de tarefas. Permite que os usuários se cadastrem, façam login e gerenciem suas tarefas diárias, incluindo adicionar, editar e excluir tarefas.

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
