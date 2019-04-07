from django.db import models
# import os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
# path = os.path.join(BASE_DIR, 'testapp')
# path = os.path.join(path, 'static')
# print(path)

# Table For Course Only
class Course(models.Model):
    Course_Name = models.CharField(max_length=20)
    Course_Duration = models.CharField(max_length=10)

    def __str__(self):
        return self.Course_Name

# This table for Section Of Course(As Per Course Content)
class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Section_Name = models.CharField(max_length=20)

    def __str__(self):
        return self.Section_Name


# This Table is for Documents(Their Title , Path)
class Document(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    Doc_Title = models.CharField(max_length=10)
    Doc_File_Path = models.FileField(upload_to='video/')


# This Table is for Users
class Student(models.Model):
    Student_First_Name = models.CharField(max_length=20)
    Student_Last_Name = models.CharField(max_length=20)
    Student_Mobile = models.IntegerField()
    Gender = models.CharField(max_length=10)
    Password = models.CharField(max_length=10)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


