from django.urls import path
from modalities import views

urlpatterns = [
    path("modalities/", views.ModalityView.as_view()),
    path("modalities/<modality_id>/", views.ModalityDetailView.as_view()),
]
