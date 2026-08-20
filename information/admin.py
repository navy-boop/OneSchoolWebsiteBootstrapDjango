from django.contrib import admin
from .models import PersonalInformation


@admin.register(PersonalInformation)
class PersonalInformationAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "name",
        "gender",
        "age",
        "email",
        "phone",
        "message",
    ]
