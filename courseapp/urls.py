from django.contrib import admin
from django.urls import path, include, re_path


urlpatterns = [
    # đi vào urls cha trống kết nối đến urls con in courses
    path('', include('courses.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
