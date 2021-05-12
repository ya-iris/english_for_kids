from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class StudentGroup(models.Model):
    name = models.CharField(max_length=10)
    year = models.IntegerField()

    class Meta:
        unique_together = ('name', 'year',)

    def __str__(self):
        return '%s%s' % (self.year, self.name)


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    parent_tel_numb = models.CharField(max_length=13, verbose_name="Parent's telephone number")
    parent_f_name = models.CharField(max_length=20, verbose_name="Parent's first name")
    parent_patronimic = models.CharField(max_length=30, verbose_name="Parent's patronimic")
    parent_l_name = models.CharField(max_length=30, verbose_name="Parent's last name")
    student_group = models.ForeignKey(StudentGroup, to_field='id', on_delete=models.SET_NULL, blank=True, null=True)

    # def __str__(self):


class Application(models.Model):
    created_at = models.DateField(auto_now_add=True)
    f_name = models.CharField(max_length=20, verbose_name="Student's first name")
    l_name = models.CharField(max_length=30, verbose_name="Student's last name")
    age = models.IntegerField(verbose_name="Student's age")
    parent_tel_numb = models.CharField(max_length=13, verbose_name="Parent's telephone number")
    parent_email = models.EmailField(max_length=254, verbose_name="Parent's email")
    parent_f_name = models.CharField(max_length=20, verbose_name="Parent's first name")
    parent_patronimic = models.CharField(max_length=30, verbose_name="Parent's patronimic")
    parent_l_name = models.CharField(max_length=30, verbose_name="Parent's last name")

    def __str__(self):
        return '%s : %s %s' % (self.created_at, self.f_name, self.l_name)


class Lesson(models.Model):
    task = models.CharField(max_length=4000)
    created_at = models.DateField(auto_now_add=True)
    student_group = models.ForeignKey(StudentGroup, to_field='id', on_delete=models.CASCADE)

    def __str__(self):
        return '%s : %s' % (self.created_at, self.student_group)


class Announcement(models.Model):
    announcement = models.CharField(max_length=4000)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s : %s' % (self.created_at, self.announcement)