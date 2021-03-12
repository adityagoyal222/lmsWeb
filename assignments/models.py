from django.db import models
from users.models import User
from courses.models import Course
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
import os
from django.conf import settings

# Create your models here.
class Assignment(models.Model):
    assignment_name = models.CharField(max_length=200, blank=False)
    assignment_description = models.TextField(blank=False)
    start_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.assignment_name