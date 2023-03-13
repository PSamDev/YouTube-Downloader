from django.urls import path
from .import views

app_name = "youtube"

urlpatterns = [
    path("", views.index, name="home"),
    path("download/", views.download, name="download"),
    path("download/<resolution>", views.yt_download_complete, name="complete"),
]
