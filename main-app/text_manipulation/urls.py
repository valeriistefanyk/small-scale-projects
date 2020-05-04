from django.urls import path
from text_manipulation import views


app_name = 'text-manipulation'
urlpatterns = [
    path('', views.count_smt_in_text, name='count-smt'),
]