from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from March5Project import settings
from testapp.models import Student, Document, Course, Section
import re
import os


def first_page(request):
    return render(request, 'first_page.html')


def register(request):
    all_course = Course.objects.all()
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        mobile = request.POST.get('mobile')
        if (re.findall("^[9|8|7|6]", mobile)) == "9" or '8' or '7' or "6":
            if len(mobile) == 10:
                mobile = mobile
                gender = request.POST.get('gender')
                password = request.POST.get('password')
                course = request.POST.get('course')
                valid_mobile = Student.objects.filter(Student_Mobile=mobile)
                if valid_mobile:
                    typo = 'Registration'
                    msg = 'This Number has been taken already!!!    '
                    return render(request, 'register.html', {'msg': msg, 'type': typo, 'course': all_course})
                course = Course.objects.get(Course_Name=course)
                global course_id
                course_id = course.id
                request.session['user_name'] = mobile
                request.session['course_id'] = course_id
                Student(Student_First_Name=fname, Student_Mobile=mobile, Gender=gender,
                        Password=password, course_id=course_id, Student_Last_Name=lname).save()
                course = Course.objects.get(id=course_id)
                typo = "Thanks"
                msg = "Registered SuccessFully "
                selected_course = Document.objects.filter(course_id=course_id)
                dit = {'course': course, 'name': fname, 'type': typo, 'msg': msg,
                       'course_name': course.Course_Name, 'selected': selected_course}
                return render(request, 'register.html', context=dit)
            else:
                msg = 'Invalid Contact number'
                typo = 'Registration'
                print("4")
                return render(request, 'register.html', {'msg1': msg, 'type': typo, 'course': all_course})
        else:
            msg = 'Invalid Contact number'
            typo = 'Registration'
            print("4")
            return render(request, 'register.html', {'msg1': msg, 'type': typo})
    typo = "Registration"
    return render(request, 'register.html', {'type': typo, 'course': all_course})


def loginview(request):
    if request.method == "POST":
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        valid_mobile = Student.objects.filter(Student_Mobile=int(mobile))
        if not valid_mobile:
            typo = 'To Login'
            msg = "The Given number isn't correct !!!"
            return render(request, 'first_page.html', {'msg': msg, 'type': typo})
        try:
            request.session["user_name"] = mobile
            valid_mobile = Student.objects.get(Student_Mobile=int(mobile), Password=str(password))
        except Student.DoesNotExist:
            typo = 'To Login'
            msg = "Wrong Password !!!"
            return render(request, 'first_page.html', {'msg': msg, 'type': typo})
        else:
            global course_id
            course_id = valid_mobile.course_id
            course_id = course_id
            request.session['course_id'] = course_id
            student_name = valid_mobile.Student_First_Name
            course = Course.objects.get(id=course_id)
            typo = "Thanks"
            selected_course = Document.objects.filter(course_id=course_id)
            dit = {'course': course, 'name': student_name, 'type': typo,
                   'course_name': course.Course_Name, 'selected': selected_course}
            return render(request, 'register.html', context=dit)
    typo = "To Login"
    return render(request, 'first_page.html', {'type': typo})


def section_detail_view(request):
    try:
        mobile = request.session["user_name"]

    except:
        return render(request, 'first_page.html')
    else:
        stud_details = Student.objects.get(Student_Mobile=mobile)
        course = stud_details.course_id
        request.session['course_id'] = course
        sect_details = Section.objects.filter(course_id=course)
        typo = "Section Response"
        course_id = request.session['course_id']
        course = Course.objects.get(id=course_id)
        my_dict = {'documents': sect_details, 'type': typo, 'course_name': course.Course_Name}
        return render(request, 'docs_detail_page.html', context=my_dict)


def docs_detail_view(request):
    id_no = request.GET.get('id')
    try:
        course_id_by_session = request.session['course_id']
        docs_details = Document.objects.get(section_id=id_no, course_id=course_id_by_session)
    except Document.DoesNotExist:

        sect_details = Section.objects.filter(course_id=course_id_by_session)
        typo = "Section Response"
        my_dict = {'documents': sect_details, 'type': typo}
        return render(request, 'docs_detail_page.html', context=my_dict)
    except:
        return render(request, 'first_page.html')

    else:
        course_id_by_session = Course.objects.get(id=course_id_by_session)
        path = docs_details.Doc_File_Path
        print('path-1', path)
        print(type(path))
        path = settings.MEDIA_URL
        # path = settings.MEDIA_ROOT + "\Akull_-_Laal_Bindi.webm"
        print('path-2', path)
        print(type(path))
        # Here I have SO many video file Extensions for Checking the extension of videos and Based on all this
        # Extensions We will be able to play video in Browser

        # find_video = re.findall('.webm', str(path))
        # |.mp4|.mkv|.flv|.vob|.gif|.gifv|.MTS|.M2TS|'.mpg|.mp2|.mpeg|.mpe|.mpv|.m4v|.nsv'

        sect_details = Section.objects.filter(course_id=course_id_by_session)
        # if find_video:
        #     print("I Found This -", find_video)
        my_dict = {'path': path, 'type': "Section Response", 'typo': "Open_Video",
                   'course_name': course_id_by_session.Course_Name, 'documents': sect_details,
                   }
        return render(request, 'docs_detail_page.html', context=my_dict)
        # find_audio = re.findall(r'.mp3', str(path).lower())
        # if find_audio:
        #     print(" Audio File", find_audio)
        #     my_dict = {'path': path, 'type': "Section Response", 'typo': "Open_Audio",
        #                'course_name': course_id_by_session.Course_Name, 'documents': sect_details,
        #                }
        #     return render(request, 'docs_detail_page.html', context=my_dict)
        # else:
        #     my_dict = {'path': path, 'type': "Section Response", 'typo': "Open_File",
        #                'course_name': course_id_by_session.Course_Name, 'documents': sect_details}
        #     return render(request, 'docs_detail_page.html', context=my_dict)


def log_out(request):
    try:
        del request.session['user_name']
        del request.session['course_id']
        request.session.modified = True
    except:
        return render(request, 'first_page.html')
    else:
        return render(request, 'first_page.html', {'session': "Successfully Logged Out"})
