from django.shortcuts import render,HttpResponse


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.GET.get('text', 'default')
    djcheckbox = request.GET.get('check', 'off')
    print(djtext)
    print(djcheckbox)
    punctuations = '''#$%&'()*+,"-./:;<=>?@[\\]^_`{|}~'''
    if djcheckbox == 'on':
        for i in punctuations:
            if i in djtext:
                djtext = djtext.replace(i, "")

        analyzed = djtext

        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
