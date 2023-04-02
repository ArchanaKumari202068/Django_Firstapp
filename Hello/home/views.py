from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable1':"this is sent",
        'variable2':"this is sent"
    }
    return render(request,"base.html",context)

def about(request):
    # return HttpResponse("this is aboutpage")
    return render(request,"about.html")
def services(request):
    return render(request,"services.html")
    # return HttpResponse("this is servicepage")
def contact(request):
    # return HttpResponse("this is contactpage")
    return render(request,"contact.html")
def home(request):
    # return HttpResponse("this is contactpage")
    return render(request,"home.html")