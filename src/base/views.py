from django.shortcuts import render, HttpResponse


# Create your views here.

def hello_world(request):
    return render(request, 'index.html', {'link': '../about'})


def about(request):
    return render(request, 'about.html', {"info": "../uzb_info"})


def uzb_info(request):
    return render(request, 'info.html', {})
