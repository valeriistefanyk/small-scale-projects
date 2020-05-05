from django.shortcuts import render


def currenttodos(request):
    """ Текущие задания """

    context = {}
    return render(request, 'todo/currenttodos.html', context)