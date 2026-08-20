# from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ("student", "学生"),
        ("parent", "家长"),
        ("teacher", "教师"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(
        max_length=20,
    )
    email = models.EmailField(max_length=254, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)

    # def __str__(self):
    #     return self.user
    def __str__(self):
        return self.user.username


# 邀请码数据类
class InviteCode(models.Model):
    code = models.CharField(max_length=50, unique=True)

    is_used = models.BooleanField(default=False)

    def __str__(self):
        return self.code



