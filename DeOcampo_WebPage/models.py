from django.db import models

# Create your models here.

class cInformations(models.Model):
    cInformation = models.SmallIntegerField
    cName = models.TextField(max_length=200)
    cStudentId = models.CharField(max_length=100)
    cAge = models.SmallIntegerField
    cDepartment = models.TextField(max_length=200)
