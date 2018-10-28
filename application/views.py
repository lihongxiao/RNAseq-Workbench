from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    #return HttpResponse("RNA")
    return render(request,"mainpage.html",)

def log(request):
    return  render(request,"login.html",)

def signUp(request):
    return render(request,"sign-up.html",)

def userpage(request):
    return render(request,"userpage.html",)

def helppage(request):
    return render(request,"help.html",)

def platPage(request):
    return render(request,"RNA sequencing.html",)

def mRNASeq(request):
    return render(request, "mRNASeq.html",)

def anaysisPage(requst):
    return render(requst, "Analysis-page.html",)
