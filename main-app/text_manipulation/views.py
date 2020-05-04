from django.shortcuts import render


def count_smt_in_text(request):

    what_count = {
        'letter': letter_count,
        'word': word_count,
    }

    text = ''
    response = ''
    what_count_choice = ''

    if request.POST.get('count'):
        text = request.POST.get('text')
        what_count_choice = request.POST.get('what_count')

        element, length = what_count[what_count_choice](text)

        response = f"Количество {element} в тексте - {length}"
    
    context = {
        'text': text,
        'what_count': what_count_choice,
        'response': response,
    }

    return render(request, 'text_manipulation/count_smt.html', context)



# helper methods
def word_count (text:str):
    if text:
        text = text.replace("\n", " ")
        text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
        text = text.lower()
        wcount = len(text.split(' '))
    else: 
        wcount = 0
    return 'слов', wcount

def letter_count (text:str):
    return 'букв', len(text)