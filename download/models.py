# Create your models here.
from django.db import models


class DownloadFile(models.Model):

    title = models.CharField(max_length=200, verbose_name="文件名称")

    file = models.FileField(upload_to="downloads/", verbose_name="文件")

    description = models.TextField(blank=True, verbose_name="文件说明")

    upload_date = models.DateField(auto_now_add=True, verbose_name="上传日期")

    def __str__(self):

        return self.title
