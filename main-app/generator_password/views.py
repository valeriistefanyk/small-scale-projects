from django.shortcuts import render
from django.http import HttpResponse
import random

def gen_pass(request):

    characters = list('qwertyuiopasdfghjklzxcvbnm')
    uppercase = list('QWERTYUIOPASDFGHJKLZXCVBNM')
    numbers = list('1234567890')
    special = list('!@#$%^&*()?/{}')

    password = ''
    default_length = 12
    default_uppercase = ''
    default_numbers = ''
    default_special = ''

    if request.method == 'GET':
        length = int(request.GET.get('length')) if request.GET.get('length') else 0
        if length:
            if request.GET.get('uppercase'):
                default_uppercase = 'on'
                characters.extend(uppercase)
            if request.GET.get('numbers'):
                default_numbers = 'on'
                characters.extend(numbers)
            if request.GET.get('special'):
                default_special = 'on'
                characters.extend(special)

            for i in range(length):
                password += random.choice(characters)
            default_length = length


    context = {
        'password': password,
        'default_length': default_length,
        'default_uppercase': default_uppercase,
        'default_numbers': default_numbers,
        'default_special': default_special,
    }

    return render(request, 'password/password.html', context)