from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('hr', 'HR'),
        ('employee', 'Employee'),
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    MARITAL_STATUS_CHOICES = (
        ('S', 'Single'),
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')
    phone_regex = RegexValidator(regex=r'^
      \+?1?\d{9,15}$', message='Phone number invalid')
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    middle_initial = models.CharField(max_length=1, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES, blank=True)
    alternate_email = models.EmailField(blank=True)
    emergency_contact = models.CharField(max_length=100, blank=True)
    emergency_phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    current_address = models.TextField(blank=True)
    permanent_address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    pincode = models.CharField(max_length=10, blank=True)
    education_level = models.CharField(max_length=100, blank=True)
    degree = models.CharField(max_length=100, blank=True)
    institution = models.CharField(max_length=200, blank=True)
    year_of_passing = models.IntegerField(null=True, blank=True)
    employee_id = models.CharField(max_length=50, unique=True, null=True, blank=True)
    position = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=200, blank=True)
    joining_date = models.DateField(null=True, blank=True)
    years_experience = models.IntegerField(default=0)
    is_active_employee = models.BooleanField(default=True)
    father_name = models.CharField(max_length=100, blank=True)
    father_occupation = models.CharField(max_length=100, blank=True)
    mother_name = models.CharField(max_length=100, blank=True)
    mother_occupation = models.CharField(max_length=100, blank=True)
    siblings = models.TextField(blank=True)
    spouse_name = models.CharField(max_length=100, blank=True)
    spouse_occupation = models.CharField(max_length=100, blank=True)
    children = models.TextField(blank=True)

    class Meta:
        db_table = 'users_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"

class Attendance(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendance_records')
    clock_in_time = models.DateTimeField(null=True, blank=True)
    clock_out_time = models.DateTimeField(null=True, blank=True)
    clock_in_image = models.ImageField(upload_to='attendance/clock_in/', null=True, blank=True)
    clock_out_image = models.ImageField(upload_to='attendance/clock_out/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'attendance_records'
        ordering = ['-created_at']
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendance Records'

    def __str__(self):
        return f"{self.employee.username} - {self.created_at.date()}"