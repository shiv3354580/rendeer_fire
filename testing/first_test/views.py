from django.shortcuts import render,HttpResponse

# Create your views here.
def helo(request):
    return HttpResponse("fly testing")