from django.db import models
from courses.models import Course

# Create your models here.
class Resource(models.Model):
    resource_name = models.CharField(max_length=200, blank=False)
    resource_file = models.FileField(blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.resource_name
