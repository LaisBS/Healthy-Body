from django.urls import path
from plans.views import PlanView, PlanDetailView

urlpatterns = [
    path("plan/", PlanView.as_view()),
    path("plan/<plan_id>/", PlanDetailView.as_view()),
]
