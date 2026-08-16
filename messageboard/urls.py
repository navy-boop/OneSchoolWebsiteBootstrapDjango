from django.urls import path
from . import views
urlpatterns = [
    path(
        "submit/",
        views.message_submit,
        name="message_submit"
    ),
]