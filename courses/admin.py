from django.contrib import admin
from django.template.response import TemplateResponse
from .models import Category, Course, Lesson, Tag
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['pk', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']


class LessonTagInline(admin.TabularInline):
    model = Lesson.tag.through


class LessonInlineAdmin(admin.StackedInline):
    model = Lesson
    pk_name = 'course'




class CourseAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all':('/static/CSS/main.css',)
        }

    inlines = (LessonInlineAdmin,)
    list_display = ['pk', 'subject', 'description']
    search_fields = ['subject']
    readonly_fields = ['img']


    def img(self, course):
        if course:
            return mark_safe(
                "<img src='/static/{url}' width='120'/>".format(url=course.image.name, alt=course.subject)
            )


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'

class LessonAdmin(admin.ModelAdmin):
    list_display =['id', 'subject', 'create_date', 'active']
    form = LessonForm

    inlines = (LessonTagInline,)


class CourseAppAdminSite(admin.AdminSite):
    site_header = 'HE THONG QUAN LY KHOA HOC'

    def get_urls(self):
        return [
            path('course-stats/', self.course_stats)
        ] + super().get_urls()


    def course_stats(self, request):
        course_count = Course.objects.count()
        return TemplateResponse(request, 'admin/course-stats.html', {
            'course_count': course_count
        })


admin_site = CourseAppAdminSite('mycourse')


admin_site.register(Category, CategoryAdmin)
admin_site.register(Course, CourseAdmin)
admin_site.register(Lesson, LessonAdmin)
admin_site.register(Tag)


