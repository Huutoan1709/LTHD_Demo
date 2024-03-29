from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
# Tham số đầu tiên luôn luôn là request

def index(request):
    return HttpResponse("Index page: HuuToan")


def welcome(request,year):
    return HttpResponse("Hello" + str(year))


def welcome2(request,year):
    return HttpResponse("Welcome " + str(year))


class TestView (View):
    def get(self,request):
        return HttpResponse("TESTTINGGG")

    def post(self, request):
        pass
