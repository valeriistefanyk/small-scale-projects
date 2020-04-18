from django.urls import path
from generator_password import views


app_name = 'password-app'
urlpatterns = [
    path('', views.gen_pass, name='password'),
]