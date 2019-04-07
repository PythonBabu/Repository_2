from django.contrib import admin
from testapp import models


class Course_Admin(admin.ModelAdmin):
    list_display = ['id', 'Course_Name', 'Course_Duration']
class Sec_Admin(admin.ModelAdmin):
    list_display = ['id', 'Section_Name', 'course_id']
class Doc_Admin(admin.ModelAdmin):
    list_display = ['id', 'Doc_Title', 'Doc_File_Path', 'course_id', 'section_id']
class StudAdmin(admin.ModelAdmin):
    list_display = ['id', 'Student_First_Name', 'Student_Last_Name', 'Student_Mobile','Gender', 'Password', 'course_id']


admin.site.register(models.Student, StudAdmin)
admin.site.register(models.Course, Course_Admin)
admin.site.register(models.Section, Sec_Admin)
admin.site.register(models.Document, Doc_Admin)