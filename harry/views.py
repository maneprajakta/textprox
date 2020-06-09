# i have created this file prajakta ...
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    #get the text
    djtext=request.POST.get('text','default')
    #checkbox value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount=request.POST.get('charcount', 'off')

    #check wich checkbox on
    if(len(djtext)==0):
        return  render(request,'error.html')
    if (removepunc=="on"):
        analyzed=""
        punctuations = '''!()-[];:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)
    if (fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {'purpose': 'CHANGED STATEMENT IN UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if (newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed+char
        params = {'purpose': 'removed newline', 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover=='on'):
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" " :
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'removed space', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if (charcount=='on'):
        analyzed = 0
        for char in djtext:
            if char != " ":
                analyzed=analyzed+1
        params = {'purpose': 'Character counted are', 'analyzed_text': analyzed}
        djtext = analyzed
    if(charcount!="on" and extraspaceremover!="on" and removepunc!="on" and newlineremover!="on" and fullcaps!="on"):
        return  render(request,'error.html')
    return render(request, 'analyze.html', params)