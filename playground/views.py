from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#request -> response
#request handler/action

def say_hello(request):
    #pull data from database, etc
    #return HttpResponse('Hello World!')
    return render(request, 'hello.html')



