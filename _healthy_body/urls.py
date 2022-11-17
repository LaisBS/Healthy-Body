"""_healthy_body URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("teachers.urls")),
    path("api/", include("personals.urls")),
    path("api/", include("customers.urls")),
    path("api/", include("users.urls")),
    path("api/", include("modalities.urls")),
    path("api/", include("private_trainings.urls")),
    path("api/", include("private_classes.urls")),
    path("api/", include("trains.urls")),
    path("api/", include("plans.urls")),
    path("api/", include("classes.urls")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger-doc/", SpectacularSwaggerView.as_view()),
    path("api/redoc/", SpectacularRedocView.as_view()),
]
