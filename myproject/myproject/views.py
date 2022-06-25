from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    content = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extrasppaceremover = request.POST.get('extrasppaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc=="on":
        punctuations = ''',./;:[]()""'!..._-?{}@#$%^&*<>'''
        analyzed = ""
        for char in content:
            if char not in punctuations:
                analyzed = analyzed+char

        param = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        content = analyzed

    if fullcaps=="on":
        analyzed = ""
        for char in content:
            analyzed = analyzed + char.upper()

        param = {'purpose':'Capitalize', 'analyzed_text':analyzed}
        content = analyzed

    if newlineremove=="on":
        analyzed = ""
        for char in content:
            if char !="\n" and char !="\r":
                analyzed += char

        param = {'purpose':'New Line Removed', 'analyzed_text':analyzed}
        content = analyzed


    if extrasppaceremover=="on":
        analyzed = ""
        for index, char in enumerate(content):
            if not(content[index]==" " and content[index+1]==" "):
                analyzed = analyzed + char

        param = {'purpose':'Entra Space Remover', 'analyzed_text':analyzed}
        content = analyzed
        # return render(request, 'analyze.html', param)


    if charcount=="on":
        analyzed =('Number of characters are ', len(content))
        
        param = {'purpose':'Charactor Count', 'analyzed_text':analyzed}
        content = analyzed

    if removepunc !="on" and fullcaps !="on" and newlineremove !="on" and extrasppaceremover !="on" and charcount !="on":
        return HttpResponse("Error")

    return render(request, 'analyze.html', param)