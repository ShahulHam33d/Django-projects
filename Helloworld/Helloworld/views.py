from django.http import HttpResponse

def show(request):
    return HttpResponse("<br><h1 align='center' style='font-size:300%'>Hello World</h1>")