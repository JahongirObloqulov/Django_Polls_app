from django.shortcuts import render, HttpResponse


# Create your views here.

def hello_world(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def uzb_info(request):
    return HttpResponse("O'zbekiston poytaxti Toshkent")
