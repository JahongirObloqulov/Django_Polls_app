from django.urls import path
from .views import *

urlpatterns = [
    path("test/", hello_world),
    path('uzb_info/', uzb_info),
    path('about/', about),
]
