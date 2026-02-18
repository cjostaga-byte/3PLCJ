from rest_framework import viewsets

# Import your models here
# from .models import User, Dashboard, Attendance

class UserViewSet(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    # serializer_class = UserSerializer

    def list(self, request):
        # Logic for listing users
        pass

class DashboardViewSet(viewsets.ModelViewSet):
    # queryset = Dashboard.objects.all()
    # serializer_class = DashboardSerializer

    def list(self, request):
        # Logic for listing dashboards
        pass

class AttendanceViewSet(viewsets.ModelViewSet):
    # queryset = Attendance.objects.all()
    # serializer_class = AttendanceSerializer

    def list(self, request):
        # Logic for listing attendance records
        pass
