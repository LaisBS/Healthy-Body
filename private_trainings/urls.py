from django.urls import path
from . import views

urlpatterns = [
    path("customer/owner/private_training/", views.PrivateViewCustomer.as_view()),
    path("private_training/", views.GetAllPrivateTrainings.as_view()),
    path("personal/owner/private_training/", views.PrivateViewPersonal.as_view()),
    path("private_training/<personal_id>/", views.PrivateSchedulePersonal.as_view()),
    path(
        "private_training/personal/<training_id>/",
        views.PrivateTrainingDetailForPersonals.as_view(),
    ),
    path(
        "private_training/customer/<training_id>/",
        views.PrivateTrainingDetailForCustomers.as_view(),
    ),
]
