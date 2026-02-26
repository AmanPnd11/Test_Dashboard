from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

# Create your models here.
class TblSuperAdmin(models.Model):
    
    AdminName = models.CharField(max_length=100)
    UserName = models.CharField(max_length=100, unique=True)
    Email = models.EmailField(unique=True)
    MobileNumber = models.CharField(max_length=15)
    Password = models.CharField(max_length=255)
    ROLE_CHOICES = (
        ('SUPER_ADMIN', 'Super Admin'),
        ('SUB_ADMIN', 'Sub Admin'),
    )
    Role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='SUPER_ADMIN'
    )

    IsActive = models.BooleanField(default=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.AdminName
        


class Department(models.Model):
    Deptname = models.CharField(max_length=100, unique=True)
    Deptcode = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.Deptname



class TblSubAdmin(models.Model):
    Subadminfirstname = models.CharField(max_length=100)
    Subadminlastname = models.CharField(max_length=100)
    Subadminemail = models.EmailField(unique=True)
    Subadminmobile = models.CharField(max_length=15)
    Subadminpassword = models.CharField(max_length=15)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    IsActive = models.BooleanField(default=True) 
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Subadminfirstname


class studentregistration(models.Model):
    
    username = models.CharField(max_length=100)
    mail = models.EmailField(unique=True)
    RollNo = models.CharField(max_length=20, unique=True)
    MobileNo = models.CharField(max_length=15)
    CreatePassword = models.CharField(max_length=15)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    IsActive = models.BooleanField(default=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Subject(models.Model):
    Subjectname = models.CharField(max_length=100)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('Subjectname', 'Department')
    
    def __str__(self):
        return self.Subjectname

class Test(models.Model):
    test_name = models.CharField(max_length=200)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_by = models.ForeignKey(TblSubAdmin, on_delete=models.CASCADE)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    def __str__(self):
        return self.test_name

class Question(models.Model):
    Test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="questions")
    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1, choices=[
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C'),
        ('D', 'Option D'),
    ])
    marks = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.question_text


class StudentResult(models.Model):
    studentregistration = models.ForeignKey(studentregistration, on_delete=models.CASCADE)
    Test = models.ForeignKey(Test, on_delete=models.CASCADE)
    total_questions = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()
    obtained_marks = models.PositiveIntegerField()
    percentage = models.FloatField()
    status = models.CharField(max_length=10)
    CreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.studentregistration.username} - {self.Test.test_name}"

