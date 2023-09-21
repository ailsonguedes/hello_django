from django.shortcuts import render,HttpResponse

# Create your views here.
def intro(request):
    return HttpResponse('<h1>Bem-Vindo a sua Célula de Aplicações Web Django</h1>\n'+
                        '<p>1. Use a url /nome/algumnome/ para acessar a pagina de hello nome.</p>\n'+
                        '<p>2. Use a url /soma/num1/num2/ para acessar a pagina de soma.</p>\n'+
                        '<p>3. Use a url /subtracao/num1/num2/ para acessar a pagina de subtração.</p>\n'+
                        '<p>4. Use a url /multiplicacao/num1/num2/ para acessar a pagina de multiplicação.</p>\n'+
                        '<p>5. Use a url /divisao/num1/num2/ para acessar a pagina de divisao.</p>\n')

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello, {}!</h1>\n<h2>Você tem {} anos.</h2>'.format(nome, idade))

def soma(request, num1, num2):
    total = num1 + num2
    return HttpResponse('<h1>Soma = {}</h1>'.format(total))

def subtracao(request, num1, num2):
    total = num1 - num2
    return HttpResponse('<h1>Subtração = {}</h1>'.format(total))

def multiplicacao(request, num1, num2):
    total = num1 * num2
    return HttpResponse('<h1>Multiplicação = {}</h1>'.format(total))

def divisao(request, num1, num2):
    total = num1 / num2
    return HttpResponse('<h1>Divisão = {}</h1>'.format(total))