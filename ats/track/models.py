from django.db import models

# Create your models here.


class Job(models.Model):
    company = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    job_desc = models.TextField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.role
