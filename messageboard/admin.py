# Register your models here.
from django.contrib import admin
from .models import Message
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "short_content",
        "created_time",
    )
    def short_content(self, obj):
        if len(obj.content) > 30:
            return obj.content[:30] + "..."
        return obj.content
    short_content.short_description = "留言内容"