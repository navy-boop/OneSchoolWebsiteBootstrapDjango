# Create your models here.
from django.db import models
class Message(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="姓名"
    )
    email = models.EmailField(
        blank=True,
        verbose_name="邮箱"
    )
    content = models.TextField(
        verbose_name="留言内容"
    )
    created_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="留言时间"
    )
    def __str__(self):
        return self.name
