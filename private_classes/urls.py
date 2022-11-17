from django.urls import path
from . import views

urlpatterns = [
    path("customer/private_class/", views.PrivateViewCustomer.as_view()),
    path("private_class/", views.GetAllPrivateClasses.as_view()),
    path("teacher/private_class/auth/", views.PrivateViewPersonal.as_view()),
    path("private_class/<teacher_id>/", views.PrivateScheduleTeacher.as_view()),
    path(
        "private_class/teacher/<class_id>/",
        views.PrivateClassesDetailForTeachers.as_view(),
    ),
    path(
        "private_class/customer/<class_id>/",
        views.PrivateClassesDetailForCustomers.as_view(),
    ),
]
