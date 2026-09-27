from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

# Create your models here.
class Student(models.Model):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Faculty Administrator'
        LECTURER = 'LECTURER', 'Lecturer'
        STUDENT = 'STUDENT', 'Student'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    role = models.CharField(choices=Role.choices, default=Role.STUDENT)
    
    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"