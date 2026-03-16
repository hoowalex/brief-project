from django.urls import path
from .views import brief_form_view, success_view

urlpatterns = [
    path("", brief_form_view, name="brief_form"),
    path("success/", success_view, name="brief_success"),
]