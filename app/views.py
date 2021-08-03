from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def random_word(request):
    if 'count' in request.session:
        request.session['count']=request.session['count']+1
    else:
        request.session['count']=1
    context = {
        "title": "Random Word",
        "word": get_random_string(length=14),
    }
    return render(request,'app/index.html', context)

def reset(request):
    request.session['count']=0
    return redirect("/")
