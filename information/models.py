# Create your models here.
from django.db import models
class PersonalInformation(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(
        max_length=10,
        blank=True
    )
    age = models.IntegerField(
        null=True,
        blank=True
    )
    email = models.EmailField()
    phone = models.CharField(
        max_length=20,
        blank=True
    )
    message = models.TextField(
        blank=True
    )
    create_time = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return self.name