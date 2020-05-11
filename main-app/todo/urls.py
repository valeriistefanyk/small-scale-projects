from django.urls import path
from todo import views


app_name = 'todo'
urlpatterns = [
    path('', views.current_todos, name='current-todos'),
    path('create/', views.create_todo, name='create-todo'),
]