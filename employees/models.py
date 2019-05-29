from django.db import models

from wagtailorderable.models import Orderable

# Create your models here.
class Employee(Orderable, models.Model):
    name = models.CharField(max_length=200)
    avatar = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    type = models.SmallIntegerField()
    position = models.CharField(max_length=200, blank=True, null=True)
    subposition = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name