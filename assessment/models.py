from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Assessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    stream = models.CharField(max_length=10)
    subject_1_name = models.CharField(max_length=50)
    subject_1_marks = models.IntegerField(default=0)
    subject_2_name = models.CharField(max_length=50)
    subject_2_marks = models.IntegerField(default=0)
    subject_3_name = models.CharField(max_length=50, default="")
    subject_3_marks = models.IntegerField(default=0)
    subject_4_name = models.CharField(max_length=50, default="")
    subject_4_marks = models.IntegerField(default=0)
    subject_5_name = models.CharField(max_length=50, default="")
    subject_5_marks = models.IntegerField(default=0)
    hollandCode1 = models.CharField(max_length=20)
    hollandCode2 = models.CharField(max_length=20)
    hollandCode3 = models.CharField(max_length=20)
    result = models.CharField(max_length=10000, default="")
