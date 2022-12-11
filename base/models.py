from django.db import models

# Create your models here.

# models.py
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        ordering = ['-end_date', '-start_date']

    def __str__(self):
        return self.name[0:50]

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        ordering = ['-end_date', '-start_date']

    def __str__(self):
        return self.name[0:50]


class TeamMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name[0:50]

