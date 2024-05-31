# from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.upload, name='upload'),
    path('run_tasks/', views.run_tasks, name='run_tasks'),
    path('download_preprocessed_dataset/', views.download_preprocessed_dataset, name='download_preprocessed_dataset'),
    path('preview/', views.preview, name='preview'),
]

