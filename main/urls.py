from django.urls import path
from main import views

urlpatterns = [
      path('teacher/', views.TeacherList.as_view()),
      path('teacherRegister/', views.TeacherRegister.as_view()),
      path('teacherlogin/', views.TeacherLogin.as_view())
]
