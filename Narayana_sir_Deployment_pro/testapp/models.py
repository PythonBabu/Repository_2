from django.db import models
from multiselectfield import MultiSelectField


class Contact_Data(models.Model):

    name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.BigIntegerField()

    Course_Choices = (
        ('py', 'python'),
        ('dj', 'django'),
        ('ui', 'user interface'),
        ('ra', 'rest api')
    )

    courses = MultiSelectField(max_length=100, choices= Course_Choices)

    Locatio_Choices = (
        ('hyd', 'hyderabad'),
        ('bang', 'banglure'),
        ('chn', 'chennai'),
    )
    location = MultiSelectField(max_length=100, choices=Locatio_Choices)

    Shift_Choices = (
        ('mor', 'morning'),
        ('aft', 'afternoon'),
        ('evn', 'evening'),
        ('nig', 'night'),
    )
    shift = MultiSelectField(max_length=100, choices=Shift_Choices)


class Feedback_Data(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField()
    feedback = models.CharField(max_length=200)
    rating = models.IntegerField()
