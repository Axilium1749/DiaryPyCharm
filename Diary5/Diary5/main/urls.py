from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index),
    path('homework', views.homework),
    path('marks', views.marks),
    path('notifications', views.notifications),
    path('teacher', views.teacher),
    path('settings', views.settings),

]
