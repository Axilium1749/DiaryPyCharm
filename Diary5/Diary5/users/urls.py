from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', login_required(views.home_view), name='home'),  # Защищаем страницу
]
