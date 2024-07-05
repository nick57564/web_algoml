from django.shortcuts import render
import tiktoken
from django.http import HttpResponse
from django.template import loader

def Base_view(request): 
    if request.method == 'POST':
        input_text = request.POST.get('name')
        if input_text:
            enc = tiktoken.get_encoding("cl100k_base") 
            tokens = enc.encode(str(input_text))
            return render(request, 'token.html', {"tokens": tokens})
        else:
            return render(request, 'token.html', {"tokens": []})

    return render(request, "home.html")


