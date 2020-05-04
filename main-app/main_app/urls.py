from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),


    path('password/', include('generator_password.urls')),
    path('text/', include('text_manipulation.urls')),
    path('todo/', include('todo.urls')),
    
    # Auth
    path('signup/', views.signupuser, name='signupuser'),

    # Index page
    path('', views.index_page, name='index-page'),
]
