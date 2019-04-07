from django.shortcuts import render

from testapp.forms import Contact_Data_Form, Feedback_Data_Form
from testapp.models import Contact_Data, Feedback_Data


def home(request):
    return render(request, 'home.html')


def contact_view(request):
    if request.method =="POST":
        form = Contact_Data_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name', '')
            email = form.cleaned_data.get('email', '')
            mobile = form.cleaned_data.get('mobile', '')
            course = form.cleaned_data.get('course', '')
            location = form.cleaned_data.get('location', '')
            shift = form.cleaned_data.get('shift', '')
            data = Contact_Data(
                name=name,
                email=email,
                mobile=mobile,
                courses=course,
                location=location,
                shift=shift,
            )
            data.save()
            form = Contact_Data_Form()
            return render(request, 'contact.html', {'form': form})
        form = Contact_Data_Form()
        return render(request, 'contact.html', {'form': form})
    form = Contact_Data_Form()
    return render(request, 'contact.html', {'form': form})


import datetime
date1 = datetime.datetime.now()

def feedback_view(request):
    if request.method == "POST":
        form = Feedback_Data_Form(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            rating = request.POST.get('rating')
            feedback = request.POST.get('feedback')
            data = Feedback_Data(
                name=name,
                rating=rating,
                feedback=feedback,
                date=date1
            )
            data.save()
            fform = Feedback_Data_Form()
            feedbacks = Feedback_Data.objects.all()
            return render(request, 'institute_feedback.html',{'form': form, 'feedbacks': feedbacks})
        form = Feedback_Data_Form
        feedbacks = Feedback_Data.objects.all()
        return render(request, 'institute_feedback.html', {'form': form, 'feedbacks': feedbacks})
    form = Feedback_Data_Form
    feedbacks = Feedback_Data.objects.all()
    return render(request, 'institute_feedback.html',{'form': form, 'feedbacks': feedbacks})


def gallery(request):
    return render(request, 'institute_gallery.html')


def services(request):
    return render(request, 'services.html')
