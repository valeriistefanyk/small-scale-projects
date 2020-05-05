from django.urls import path
from todo import views


app_name = 'todo'
urlpatterns = [
    path('', views.currenttodos, name='currenttodos'),
]