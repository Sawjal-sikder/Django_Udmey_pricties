from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def january(request):
    return HttpResponse('Hello World!')

def february(request):
    return HttpResponse('atlist walking 20 munite everyday')