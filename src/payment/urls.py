from django.urls import path
from .views import *

urlpatterns = [
    path("pay/", pay),
    path('balans/', balans),
    path('info/', info),
]
