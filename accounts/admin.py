# from django.contrib import admin
# from .models import UserProfile
# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ("user", "role", "phone")
from django.contrib import admin
from django.http import HttpResponse
from openpyxl import Workbook
from .models import UserProfile
from .models import InviteCode
def export_user_profiles(modeladmin, request, queryset):
    # 创建 Excel 工作簿
    workbook = Workbook()
    # 获取当前工作表
    worksheet = workbook.active
    worksheet.title = "User Profiles"
    # Excel 表头
    worksheet.append([
        "ID",
        "用户名",
        "手机号",
        "邮箱",
        "角色"
    ])
    # 写入数据
    for profile in queryset:
        worksheet.append([
            profile.id,
            profile.user.username,
            profile.phone,
            profile.user.email,
            profile.get_role_display()
        ])
    # 设置下载响应
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = (
        'attachment; filename="user_profiles.xlsx"'
    )
    # 保存到响应
    workbook.save(response)
    return response
export_user_profiles.short_description = "导出选中的用户资料为 Excel"
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "get_username",
        "age",
        "email",
        "phone",
        "get_email",
        "role",
    )
    actions = [export_user_profiles]
    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = "用户名"
    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = "邮箱"




admin.site.register(InviteCode)