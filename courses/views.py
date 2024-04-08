from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .models import Course, Category, Lesson
from .serializers import CourseSerializer


# Create your views here.
# Tham số đầu tiên luôn luôn là request


def index(request):
    return HttpResponse("Index page: HuuToan")


def welcome(request, year):
    return HttpResponse("Hello" + str(year))


def welcome2(request, year):
    return HttpResponse("Welcome " + str(year))


class TestView(View):
    def get(self, request):
        return HttpResponse("TESTTINGGG")

    def post(self, request):
        pass


class CourseViewset(viewsets.ModelViewSet):
    # Lay cac khoa hoc dang hoat dong
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer

    # list(GET) --> Danh sach khoa học active
    # (POST) --> Them khoa hoc
    # detail --> Chi tiet 1 khao hoc
    # Delete --> Xoa 1 khoa hoc
    # (PUT) -->Cap nhap khoa hoc

    # Chung Thuc da dang nhap chua
    # permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'list': #Neu xem danh sach thi khong can chung thuc dang nhap
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
