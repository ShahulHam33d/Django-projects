from django.http import HttpResponse
from django.shortcuts import render

def show(request):
    params = {'name':'shahul','place':'mysore'}
    return render(request,'index.html',params)
    #return HttpResponse("Hello world <a href = '/showtwo'>again</a>")

def showtwo(request):
    return HttpResponse("Hello again <a href='/'>back</a>")