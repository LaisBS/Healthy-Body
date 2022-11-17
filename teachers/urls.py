from django.urls import path
from . import views

urlpatterns = [
    path("teacher/", views.TeacherView.as_view()),
    path("teacher/<teacher_id>/", views.TeacherDetailView.as_view()),
]
