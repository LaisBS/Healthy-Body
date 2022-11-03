from django.urls import path

from trains import views

urlpatterns = [
    path("trains/", views.CreateListTrainView.as_view()),
    path("trains/<train_id>/", views.RetrieveUpdateDestroyTrainView.as_view()),
]
