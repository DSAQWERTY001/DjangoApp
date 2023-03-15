import uuid
from django.db import models

# Create your models here.

class School(models.Model):
    ID = models.AutoField(primary_key=True)
    school_Name = models.CharField(max_length=20)
    maximum = models.PositiveIntegerField()

    def __str__(self):
        return self.school_Name


class Student(models.Model):
    id = models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4, editable=False)
    student_ID = models.CharField(max_length=20)
    first_Name = models.CharField(max_length=20)
    last_Name = models.CharField(max_length=20)
    school = models.ForeignKey("School",on_delete=models.CASCADE,related_name="students")
    # school_id = models.PositiveBigIntegerField()

    class Meta:
        unique_together = ['school','student_ID']
    
    def __int__(self):
        return self.id