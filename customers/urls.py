from django.urls import path

from customers import views

urlpatterns = [
    path("customers/", views.CreateListCustomerView.as_view()),
    path("customers/<customer_id>/", views.RetrieveUpdateDeleteCustomerView.as_view()),
]
