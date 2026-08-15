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
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )
    phone = models.CharField(
        max_length=20,
        unique=True
    )
    email = models.EmailField(
    max_length=254,
    blank=True
    )
    age = models.PositiveIntegerField(
    null=True,
    blank=True
    )
    # def __str__(self):
    #     return self.user
    def __str__(self):
        return self.user.username
# =========================
# 新闻
# =========================
class News(models.Model):
    CATEGORY_CHOICES = [
        ("school", "学校新闻"),
        ("activity", "校园活动"),
        ("education", "教育教学"),
        ("student", "学生动态"),
        ("notice", "通知公告"),
    ]
    title = models.CharField(
        max_length=200,
        verbose_name="新闻标题"
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="school",
        verbose_name="新闻分类"
    )
    image = models.ImageField(
        upload_to="news/",
        blank=True,
        null=True,
        verbose_name="新闻图片"
    )
    summary = models.TextField(
        blank=True,
        verbose_name="新闻摘要"
    )
    content = models.TextField(
        verbose_name="新闻内容"
    )
    publish_date = models.DateField(
        auto_now_add=True,
        verbose_name="发布日期"
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name="是否发布"
    )
    class Meta:
        ordering = ["-publish_date"]
        verbose_name = "新闻"
        verbose_name_plural = "新闻"
    def __str__(self):
        return self.title