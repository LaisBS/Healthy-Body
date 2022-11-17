from django.urls import path
from classes import views

urlpatterns = [
    path("class/", views.ClassView.as_view()),
    path("class/open/", views.ListOpenClassView.as_view()),
    path("class/<class_id>/", views.ClassDetailView.as_view()),
    path("class/join/<class_id>/", views.ClassAddCustomerView.as_view()),
    path("class/remove/<class_id>/", views.ClassRemoveCustomerView.as_view()),
]
