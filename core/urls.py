from django.urls import path
from .views import home, dia_da_semana, editar_tarefa, excluir_tarefa, register, user_login, confirm_logout, delete_account
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', user_login, name='login'),  # Página inicial é a página de login
    path('home/', home, name='home'),
    path('dia/<str:dia>/', dia_da_semana, name='dia_da_semana'),
    path('editar/<int:id>/', editar_tarefa, name='editar_tarefa'),
    path('excluir/<int:id>/', excluir_tarefa, name='excluir_tarefa'),
    path('register/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL para logout
    path('confirm_logout/', confirm_logout, name='confirm_logout'),  # URL para confirmar logout
    path('delete_account/', delete_account, name='delete_account'),  # URL para excluir conta
]
