from django.shortcuts import render
from pytube import YouTube
import os

# Create your views here.
def index(request):
    return render(request, "index.html")

def download(request):
    global url
    url = request.GET.get("url")
    yt = YouTube(url)
    video = []
    video = yt.streams.filter(progressive=True).all()
    embed_link = url.replace("watch?v", "embed/")
    Title = yt.title
    context = {"video":video, "embed":embed_link, "title":Title}
    
    return render(request, "download.html", context=context)

def yt_download_complete(request, resolution):
    global url 
    homedir = os.path.expanduser("~")
    dirs = homedir + "/Downloads"
    
    if request.method == "POST":
        YouTube(url).streams.get_by_resolution(resolution).download(dirs)
        return render(request, "complete.html")
    else:
        return render(request, "404.html")