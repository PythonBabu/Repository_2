from django import forms
from multiselectfield import MultiSelectFormField


class Contact_Data_Form(forms.Form):

    name = forms.CharField(
        label= 'Enter Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Name::'
            }
        )
    )
    email = forms.EmailField(
        label= 'Enter Email id',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Email id::'
            }
        )
    )
    mobile = forms.IntegerField(
        label= 'Enter Mobile number',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Mobile Number::'
            }
        )
    )
    Course_Choices = (
        ('py', 'python'),
        ('dj', 'django'),
        ('ui', 'user interface'),
        ('ra', 'rest api')
    )
    courses = MultiSelectFormField(max_length=100, choices=Course_Choices)

    Locatio_Choices = (
        ('hyd', 'hyderabad'),
        ('bang', 'banglure'),
        ('chn', 'chennai'),
    )
    location = MultiSelectFormField(max_length=100, choices=Locatio_Choices)

    Shift_Choices = (
        ('mor', 'morning'),
        ('aft', 'afternoon'),
        ('evn', 'evening'),
        ('nig', 'night'),
    )
    shift = MultiSelectFormField(max_length=100, choices=Shift_Choices)

class Feedback_Data_Form(forms.Form):
    name = forms.CharField(
        label='Enter Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Name::'
            }
        )
    )
    rating = forms.IntegerField(
        label='Your Rating-',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Rating Here...'
            }
        )
    )
    feedback = forms.CharField(
        label='Your FeedBack ->',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Feedback here...'
            }
        )
    )