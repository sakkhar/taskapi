from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=200, null=True, blank=True, verbose_name=("task_name"))
    task_desc = models.TextField(null=True, blank=True, verbose_name=("task_desc"))
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_name

