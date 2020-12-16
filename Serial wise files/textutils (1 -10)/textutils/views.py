# I have creaed this website - Ahsanul Kabir    ---> # code for video : 3

# code for video : 4
from django.http import HttpResponse

def index_func(request):
    return HttpResponse('hello, kabir')

def about_func(request):
    return HttpResponse('About kabir...')
# code for video : 4



# code for video : 5
def html_func(request):
    return HttpResponse('<h1> Hi django <h1>')

def read_file_func(request):
    with open(r"C:\Users\Nayeem\Python & ML\Self_Django\textutils\textutils\txt.txt", "r") as f:
        m = f.read()
    return HttpResponse(m)
# code for video : 5



# code for video : 6
def navigator_func(request):
    s = '''<h2>Navigation Bar</h2>
               <a href="https://www.youtube.com/channel/UCAKvgzCzRkBTljabreyKrmg/playlists?view_as=subscriber">ML with Ahsanul Kabir</a><br> 
               <a href="https://www.facebook.com/">Facebook</a><br>
               <a href="https://www.amazon.com.au//">Amazon Australia</a><br>
               <a href="https://stackoverflow.com/">Stackoverflow</a><br>
               <a href="https://www.google.com/">Google</a>'''
    return HttpResponse(s)
# code for video : 6



# code for video : 7

def index(request):
    return HttpResponse("Home")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("capitalize first")

def spaceremove(request):
    return HttpResponse("space remover <a href='/'> Back</a>")

def charcount(request):
    return HttpResponse("charcount ")
# code for video : 7


# code for video : 8
from django.shortcuts import render
def tem_fun(request):
    parameter = {'name': 'Ahsanul Kabir', 'place':'Bangladesh'}
    return render(request, 'test.html', parameter)
# code for video : 8



# code for video : 9
def html9_func(request):
    return render(request, 'test.html')

def removepunc(request):
    #Get the text
    djtext = request.GET.get('text_area', 'default')
    print(djtext)
    #Analyze the text
    return HttpResponse("remove punc")
# code for video : 9



# code for video : 10
def html10_func(request):
    return render(request, 'test.html')

def analyze(request):
    #Get the text
    djtext = request.GET.get('text_area', 'default')
    print(djtext)
    removepunc = request.GET.get('removepunc', 'off')
    print(djtext)

#if removepunc == "on":
    #analyzed = djtext
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""

    for char in djtext:
        if char not in punctuations:
            analyzed = analyzed + char

    parameter = {'purpuse':'Remove puntuation', 'analyze_text':analyzed}
    #Analyze the text
    return render(request,'analyze.html',parameter)
#else:
    # return HttpResponse("Error")
# code for video : 10