
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepuncV = request.GET.get('removepunc', 'off')
    fullcapsV = request.GET.get('fullcaps','off')
    newlineremoverV = request.GET.get('newlineremover','off')
    extraspaceremoverV = request.GET.get('extraspaceremover','off')
    charcountV = request.GET.get('charcount', 'off')

    #check which checkbox is on
    if removepuncV =='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        parameter = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html',parameter)

    elif(fullcapsV =='on'):
        analyzed = ""

        for char in djtext:
            analyzed = analyzed + char.upper()

        parameter = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request,'analyze.html', parameter)

    elif(newlineremoverV =='on'):
        analyzed = ""

        for char in djtext:
            char = char.rstrip("\n")
            analyzed = analyzed + char

        parameter = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request,'analyze.html', parameter)

    elif(extraspaceremoverV =='on'):
        analyzed = ""

        for index,char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char

        parameter = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request,'analyze.html', parameter)


    elif(extraspaceremoverV =='on'):
        analyzed = ""

        for index,char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char

        parameter = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request,'analyze.html', parameter)

    elif(charcountV =='on'):
        analyzed = len(djtext)

        parameter = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        return render(request,'analyze.html', parameter)


    else:
        return HttpResponse("Error")


