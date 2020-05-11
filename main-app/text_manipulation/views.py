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

        count_smt_dict = what_count[what_count_choice](text)

        response = f"Количество {count_smt_dict['value']} в тексте - {count_smt_dict['count']}"
        response += f". Из них количество уникальных - {count_smt_dict['uniqwcount']}" if count_smt_dict['uniqwcount'] else ''
    
    context = {
        'text': text,
        'what_count': what_count_choice,
        'response': response,
    }

    return render(request, 'text_manipulation/count_smt.html', context)



# helper methods
def word_count (text:str):
    
    wcount_dict = {
        'value': 'слов',
        'count': 0,
        'uniqwcount': 0,
    }
    if text:
        text = text.replace("\n", " ")
        text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
        text = text.lower()

        text_arr = text.split(' ')
        wcount_dict['count'] = len(text_arr)
        print(list({i for i in text.split(' ')}))
        wcount_dict['uniqwcount'] = len(list({i for i in text_arr}))

    return wcount_dict

def letter_count (text:str):
    lcount_dict = {
        'value': 'букв',
        'count': len(text),
        'uniqwcount': None,
    }
    return lcount_dict