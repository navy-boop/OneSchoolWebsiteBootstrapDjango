from django.contrib import admin
from .models import News
from .models import Notice

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "publish_date"
    ]




@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "publish_date",
    )