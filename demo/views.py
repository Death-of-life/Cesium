from django.shortcuts import render

# Create your views here.
# demo/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("请求路径:{}" .format(request.path))

def demo(request):
    return render(request, 'demo.html')

def cesium(request):
    return render(request, 'index.html')