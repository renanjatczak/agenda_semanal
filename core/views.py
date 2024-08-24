from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

@login_required
def home(request):
    return render(request, "index.html")

@login_required
def dia_da_semana(request, dia):
    if request.method == "POST":
        tarefa = request.POST.get("tarefa")
        horario_inicio = request.POST.get("horario_inicio")
        horario_fim = request.POST.get("horario_fim")
        
        # Validação dos campos
        if not tarefa or not horario_inicio or not horario_fim:
            context = {
                'dia': dia,
                'tarefas': Tarefa.objects.filter(dia=dia, user=request.user),
                'error_message': 'Todos os campos devem ser preenchidos.'
            }
            return render(request, "dia.html", context)
        
        try:
            nova_tarefa = Tarefa(dia=dia, tarefa=tarefa, horario_inicio=horario_inicio, horario_fim=horario_fim, user=request.user)
            nova_tarefa.save()
        except ValidationError as e:
            context = {
                'dia': dia,
                'tarefas': Tarefa.objects.filter(dia=dia, user=request.user),
                'error_message': str(e)
            }
            return render(request, "dia.html", context)
        
        return redirect("dia_da_semana", dia=dia)

    tarefas = Tarefa.objects.filter(dia=dia, user=request.user)
    context = {
        'dia': dia,
        'tarefas': tarefas
    }
    return render(request, "dia.html", context)

@login_required
def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, user=request.user)
    if request.method == "POST":
        tarefa_nova = request.POST.get("tarefa")
        horario_inicio_novo = request.POST.get("horario_inicio")
        horario_fim_novo = request.POST.get("horario_fim")
        
        # Valida se os campos estão preenchidos
        if not tarefa_nova or not horario_inicio_novo or not horario_fim_novo:
            return render(request, "editar_tarefa.html", {
                'tarefa': tarefa,
                'error': 'Todos os campos são obrigatórios.'
            })
        
        # Atualiza a tarefa
        tarefa.tarefa = tarefa_nova
        tarefa.horario_inicio = horario_inicio_novo
        tarefa.horario_fim = horario_fim_novo
        tarefa.save()
        
        return redirect("dia_da_semana", dia=tarefa.dia)

    context = {'tarefa': tarefa}
    return render(request, "editar_tarefa.html", context)

@login_required
def excluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, user=request.user)
    if request.method == "POST":
        tarefa.delete()
        return redirect("dia_da_semana", dia=tarefa.dia)

    context = {'tarefa': tarefa}
    return render(request, "excluir_tarefa.html", context)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def confirm_logout(request):
    return render(request, 'confirm_logout.html')

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request)  # Faz logout do usuário
        user.delete()    # Exclui o usuário
        return redirect('login')  # Redireciona para a página de login

    return render(request, 'delete_account.html')
