from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ukoly/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
]
