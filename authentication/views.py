from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# # Cadastro de usuário
# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'authentication/register.html', {'form': form})

# Login de usuário
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout de usuário
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

# Proteção CSRF e segurança
# O Django já protege automaticamente contra CSRF quando usado corretamente

# Templates básicos
# authentication/templates/authentication/login.html
# authentication/templates/authentication/register.html
# authentication/templates/authentication/logout.html
