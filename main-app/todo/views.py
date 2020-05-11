from django.shortcuts import render, redirect, get_object_or_404
from todo.forms import TodoForm
from todo.models import Todo


def current_todos(request):
    """ Текущие задания """

    context = {}

    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True) \
                        .order_by('-important', '-created')
    context['todos'] = todos
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


def view_todo(request, todo_pk):
    """ Отображение конкретного """

    context = {}

    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    context['todo'] = todo

    return render(request, 'todo/view_todo.html', context)