from django.shortcuts import render, redirect, get_object_or_404
from todo.forms import TodoForm
from todo.models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required
def current_todos(request):
    """ Текущие задания """

    context = {}

    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True) \
                        .order_by('-important', '-created')
    context['todos'] = todos
    return render(request, 'todo/current_todos.html', context)


@login_required
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


@login_required
def view_todo(request, todo_pk):
    """ Отображение конкретного """

    context = {}

    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    context['todo'] = todo

    if request.method == 'GET':
        context['form'] = TodoForm(instance=todo)

        return render(request, 'todo/view_todo.html', context)
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('todo:current-todos')

        except ValueError:
            context['form'] = form
            context['error'] = 'Что-то пошло не так... Попробуйте заполнить поля заново'
            return render(request, 'todo/viewtodo.html', context)



@login_required
def complete_todo(request, todo_pk):
    """ Выполнить задание """

    context = {}

    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == "POST":
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('todo:current-todos')


@login_required
def delete_todo(request, todo_pk):
    """ Удалить задание """

    context = {}

    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == "POST":
        todo.delete()
        return redirect('todo:current-todos')


@login_required
def completed_todos(request):

    context = {}
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False) \
                        .order_by('-datecompleted')
    context['todos'] = todos
    return render(request, 'todo/completed_todos.html', context)