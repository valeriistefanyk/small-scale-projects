from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def index_page(request):
    """ Стартовая страница """

    return render(request, 'core/index.html')


def signupuser(request):
    """ Регистрация пользователя """

    context = {}
    if request.method == 'GET':
        context['form'] = UserCreationForm()
        return render(request, 'core/signupuser.html', context)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                login(request, user)
                return redirect('index-page')
            except IntegrityError:
                context['error'] = f'Пользователь с юзернеймом {request.POST["username"]} уже существует. Пожалуйста, выберите другое имя!'
                context['form'] = UserCreationForm()
        else:
            context['error'] = 'Пароли не совпадают!'
            context['form'] = UserCreationForm()

    return render(request, 'core/signupuser.html', context)


@login_required
def logoutuser(request):
    """ Выйти из аккаунта """

    if request.method == 'POST':
        logout(request)
        return redirect('index-page')


def loginuser(request):
    """ Логин """

    context = {}
    context['form'] = AuthenticationForm()

    if request.GET:  
        next = request.GET['next']

    if request.method == 'POST':
        
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            context['error'] = 'Логин или пароль не подходят!'
        else:
            login(request, user)
            if next:
                return redirect(next)
            return redirect('index-page')

    return render(request, 'core/loginuser.html', context)
