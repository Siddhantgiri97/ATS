
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('job_profiles/', views.job_profile, name="job_profile"),
    path('view_profile/<int:pk>/', views.view_profile, name="view_profile"),

]
