from django.db import  models
from .classes import Class

class Students(models.Model):
    username = models.CharField(max_length=20, default="ST")
    password = models.CharField(max_length=500, default="")
    admission_no = models.CharField(max_length=30, default="", unique=True)
    first_name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")
    father_name = models.CharField(max_length=30, default="")
    mother_name = models.CharField(max_length=30, default="")
    address = models.TextField()
    country = models.CharField(max_length=20, default="")
    state = models.CharField(max_length=20, default="")
    city = models.CharField(max_length=20, default="")
    zipcode = models.CharField(max_length=10, default="")
    phone = models.CharField(max_length=30, default="")
    gender = models.CharField(max_length=6, default="")
    dob = models.CharField(max_length=20)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    section = models.CharField(max_length=2, default="")
    image = models.ImageField(upload_to="student", blank=True , null=True)
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)



    def __str__(self):
        return self.username


