from django.shortcuts import render, HttpResponse


# Create your views here.

def pay(request):
    return HttpResponse('Hisobingiz to\'ldirildi.')


def balans(request):
    return HttpResponse('Hisobingizda 1 mlrd so\'m pul bor.')


def info(request):
    return HttpResponse('Hisobingizdan pul yechildi.')
