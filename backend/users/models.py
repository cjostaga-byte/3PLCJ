from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Custom user fields can be added here
    pass


class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])

    def __str__(self):
        return f'{self.user.username} - {self.date} - {self.status}'