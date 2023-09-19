from django.shortcuts import render,HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1>Hello, {}!</h1>\n<h2>Você tem {} anos.</h2>'.format(nome, idade))