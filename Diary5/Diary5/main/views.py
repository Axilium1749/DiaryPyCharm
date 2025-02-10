from .models import Day
from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import RegistrationForm
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
from .models import Student, Schedule
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def get_week_dates(start_date):
    """Возвращает список дат для текущей недели, начиная с понедельника."""
    return [start_date + timedelta(days=i) for i in range(6)]

@login_required
def index(request, student_id, week_offset=0):
    student = get_object_or_404(Student, id=student_id)
    school_class = student.school_class

    # Получаем текущую дату и корректируем её на начало недели (понедельник)
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday()) + timedelta(weeks=week_offset)

    # Получаем даты для текущей недели
    week_dates = get_week_dates(start_of_week)

    # Получаем расписание для класса ученика
    schedule = Schedule.objects.filter(school_class=school_class)

    # Создаем список дней с расписанием и датами
    days_with_schedule = []
    for date in week_dates:
        day_of_week = date.strftime('%A')
        day_schedule = schedule.filter(day_of_week=day_of_week).order_by('lesson_number')
        days_with_schedule.append({
            'date': date.strftime('%d %b'),  # Формат "ДД ммм."
            'day_of_week': day_of_week,
            'schedule': day_schedule
        })
        # Формируем диапазон дат для заголовка (например, "13 - 19 Января")
        date_range = f"{week_dates[0].strftime('%d %b')} - {week_dates[-1].strftime('%d %b')}"

        context = {
            'student': student,
            'days_with_schedule': days_with_schedule,
            'date_range': date_range,
            'week_offset': week_offset,
            'next_week_offset': week_offset + 1,
            'prev_week_offset': week_offset - 1,
        }

        return render(request, 'main/index.html', context)
@login_required
def homework(request):
    return render(request, 'main/homework.html')

@login_required
def marks(request):
    return render(request, 'main/marks.html')

@login_required
def notifications(request):
    return render(request, 'main/notifications.html')

@login_required
def settings(request):
    return render(request, 'main/settings.html')

@login_required
def teacher(request):
    return render(request, 'main/teacher.html')




