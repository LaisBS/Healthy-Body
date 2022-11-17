from django.urls import path

from personals import views

urlpatterns = [
    path("personal/", views.CreateListPersonal.as_view()),
    path("personal/<personal_id>/", views.RetrievePatchDeletePersonal.as_view()),
]
