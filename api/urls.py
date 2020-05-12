from django.urls import path
from . import views

urlpatterns = [
    # list or register schedules
    path('schedules/', views.ScheduleListCreateAPIView.as_view()),
    # retrieve, put, patch or delete schedules
    path('schedules/<pk>/', views.ScheduleRetrieveUpdateDestroyAPIView.as_view()),
]