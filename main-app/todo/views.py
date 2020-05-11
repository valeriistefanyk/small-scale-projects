from django.shortcuts import render, redirect
from todo.forms import TodoForm


def current_todos(request):
    """ Текущие задания """

    context = {}
    return render(request, 'todo/current_todos.html', context)


def create_todo(request):
    """ Создание задания """
    
    context = {}

    if request.method == 'GET':
        context['form'] = TodoForm()
        return render(request, 'todo/create_todo.html', context)
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
        except ValueError:
            context['form'] = TodoForm()
            context['error'] = 'Не верно введенные данные. Попробуйте заново!'
            return render(request, 'todo/create_todo.html', context)
        return redirect('todo:current-todos')
    