from django.db import models

# Create your models here.
def student_info(Model.models):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    pnumber = models.IntegerField()
    rnumber = models.IntegerField()