from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path("customer/private/auth/",views.PrivateViewCustomer.as_view()),
    path("private_training/",views.GetAllPrivateTrainings.as_view()),
    path("personal/private/auth/",views.PrivateViewPersonal.as_view()),
    path("private_training/<uuid:personal_id>",views.PrivateSchedulePersonal.as_view()),
    path("private_training/personal/<uuid:training_id>",views.PrivateTrainingDetailForPersonals.as_view()),
    path("private_training/customer/<uuid:training_id>",views.PrivateTrainingDetailForCustomers.as_view()),
=======
    path("customer/private/auth/", views.PrivateViewCustomer.as_view()),
    path("private_training/", views.GetAllPrivateTrainings.as_view()),
    path("personal/private/auth/", views.PrivateViewPersonal.as_view()),
    path(
        "private_training/personal/<uuid:training_id>",
        views.PrivateTrainingDetailForPersonals.as_view(),
    ),
    path(
        "private_training/customer/<uuid:training_id>",
        views.PrivateTrainingDetailForCustomers.as_view(),
    ),
>>>>>>> 33ef5eb053fc6a5451c0b04efb463db556e7270d
]
