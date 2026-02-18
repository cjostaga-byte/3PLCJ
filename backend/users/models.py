from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    attendance_records = models.JSONField(default=dict)

    def record_attendance(self, date, status):
        self.attendance_records[date] = status
        self.save()

    def get_attendance(self):
        return self.attendance_records