from django.db import models
from datetime import datetime
import locale

from django.db.models import TextField
from babel.dates import format_date
from django.contrib.auth.models import AbstractUser
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

def get_current_date_formatted():
    return format_date(datetime.now(), format="d MMM", locale='ru')

class Day(models.Model):
    date_field = models.CharField(
        max_length=10,
        default=get_current_date_formatted,
        verbose_name="Текущая дата"
    )
    day_field = models.TextField(max_length=15, null=False)
    lesson1 = TextField('Урок 1', max_length=20, blank=True, null=True)
    lesson1_mark = TextField('Оценка 1', max_length=2, blank=True, null=True)
    lesson2 = TextField('Урок 2', max_length=20, blank=True, null=True)
    lesson2_mark = TextField('Оценка 2', max_length=2, blank=True, null=True)
    lesson3 = TextField('Урок 3', max_length=20, blank=True, null=True)
    lesson3_mark = TextField('Оценка 3', max_length=2, blank=True, null=True)
    lesson4 = TextField('Урок 4', max_length=20, blank=True, null=True)
    lesson4_mark = TextField('Оценка 4', max_length=2, blank=True, null=True)
    lesson5 = TextField('Урок 5', max_length=20, blank=True, null=True)
    lesson5_mark = TextField('Оценка 5', max_length=2, blank=True, null=True)
    lesson6 = TextField('Урок 6', max_length=20, blank=True, null=True)
    lesson6_mark = TextField('Оценка 6', max_length=2, blank=True, null=True)
    lesson7 = TextField('Урок 7', max_length=20, blank=True, null=True)
    lesson7_mark = TextField('Оценка 7', max_length=2, blank=True, null=True)
    lesson8 = TextField('Урок 8', max_length=20, blank=True, null=True)
    lesson8_mark = TextField('Оценка 8', max_length=2, blank=True, null=True)

    def __str__(self):
        return self.date_field

class User(AbstractUser):
    # Добавляем related_name, чтобы избежать конфликта с другой моделью User
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_set",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions_set",
        blank=True
    )

    def __str__(self):
        return self.username

class SchoolClass(models.Model):
    name = models.CharField(max_length=3)
    class_teacher = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True, related_name="class_teacher")  # Учитель, ведущий класс

    def __str__(self):
        return self.name

from django.conf import settings
from django.db import models

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student_profile")
    full_name = models.CharField(max_length=255)
    school_class = models.ForeignKey('SchoolClass', on_delete=models.CASCADE, related_name="students")

    def __str__(self):
        return f"{self.full_name} ({self.school_class})"

from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Поле CharField

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="teacher_profile")
    subjects = models.ManyToManyField('Subject', related_name="teachers")

    def __str__(self):
        return f"{self.user.get_full_name()}"

class Schedule(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Понедельник'),
        ('Tuesday', 'Вторник'),
        ('Wednesday', 'Среда'),
        ('Thursday', 'Четверг'),
        ('Friday', 'Пятница'),
        ('Saturday', 'Суббота'),
    ]

    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE,
                                     related_name="schedule")  # Класс, к которому привязано расписание
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)  # Предмет, который преподается
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,
                                related_name="schedule")  # Учитель, преподающий этот предмет
    day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)  # День недели
    lesson_number = models.PositiveSmallIntegerField()  # Номер урока (1-8)

    class Meta:
        unique_together = ['school_class', 'day_of_week', 'lesson_number']  # Уникальность расписания для каждого класса

    def __str__(self):
        return f"{self.school_class} - {self.subject} ({self.day_of_week}, урок {self.lesson_number})"

class Grade(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='grades')  # Ученик
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)  # Предмет
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='grades')  # Учитель
    grade = models.PositiveSmallIntegerField(choices=[(2, '2'), (3, '3'), (4, '4'), (5, '5')])  # Оценка (только 2, 3, 4, 5)
    coefficient = models.PositiveIntegerField(default=1)  # Коэффициент (сколько раз учитывается эта оценка, по умолчанию 1)
    date_received = models.DateField(auto_now_add=True)  # Дата выставления

    def get_total_grade(self):
        """Возвращает сумму оценок с учетом коэффициента"""
        return self.grade * self.coefficient

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.grade} (Коэффициент: {self.coefficient})"