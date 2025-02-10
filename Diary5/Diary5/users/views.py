from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import CustomUser
from main.models import Student  # Импортируем модель Student

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Перенаправление после входа
        else:
            messages.error(request, 'Неверный логин или пароль.')
    return render(request, 'login.html')  # Используем ваш `login.html`

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Сохраняем пользователя с ролью "student"
            Student.objects.create(user=user, full_name=user.username)  # Создаем профиль Student
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Перенаправляем на страницу входа после выхода

@login_required
def home_view(request):
    user = request.user
    if user.role == 'student':
        student = user.student_profile  # Получаем профиль ученика
        return render(request, 'main/index.html', {'student': student})
    elif user.role == 'teacher':
        teacher = user.teacher_profile  # Получаем профиль учителя
        return render(request, 'main/teacher.html', {'teacher': teacher})