from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    
    # Add the role field with a default of 'student'
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')