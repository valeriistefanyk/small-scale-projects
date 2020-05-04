from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            return render(request, 'core/signupuser.html', context)
        else:
            # tell the user the passwords didn't match
            pass