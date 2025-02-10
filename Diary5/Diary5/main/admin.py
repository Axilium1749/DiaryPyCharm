from django.contrib import admin
from .models import Day, User, SchoolClass, Student, Subject, Teacher, Schedule, Grade


admin.site.register(Day)
admin.site.register(User)
admin.site.register(SchoolClass)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Schedule)
admin.site.register(Grade)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Убедитесь, что 'name' отображается в админке
