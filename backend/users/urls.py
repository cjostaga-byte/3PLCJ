from django.urls import path

from .views import AuthenticationView, AttendanceView

urlpatterns = [
    path('auth/', AuthenticationView.as_view(), name='authentication'),
    path('attendance/', AttendanceView.as_view(), name='attendance'),
]