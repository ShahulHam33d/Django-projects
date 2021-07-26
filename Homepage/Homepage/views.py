from django.shortcuts import HttpResponse,render

def show(request):
    return HttpResponse("Shahul Hameed <br> <a href = '/template'>goto_template</a>")

def template(request):
    return render(request,'index.html')

def getting(request):
    djtext =  request.GET.get('text','default')
    return HttpResponse(djtext+"<br> <a href = '/template'>goto_template</a>")