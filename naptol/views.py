from django.shortcuts import render,HttpResponse

# Create your views here.
def hello(request):
    #return HttpResponse("Hello")
    return render(request,'home.html')
