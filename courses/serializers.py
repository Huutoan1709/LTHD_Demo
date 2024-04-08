from rest_framework.serializers import ModelSerializer
from .models import Course, Category,Lesson,Tag

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ["id","subject","image","create_date","category"]

