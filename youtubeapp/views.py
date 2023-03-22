from django.shortcuts import render
from pytube import YouTube
import os
# Create your views here.

def index(request):
	return render(request,'index.html')


def download(request):
	global url
	url = request.GET.get('url')
	yt=YouTube(url)
	video=[]
	video=yt.streams.filter(progressive=True).all()
	embed_link=url.replace("watch?v=","embed/")
	Title=yt.title
	context={'video':video,'embed':embed_link,'title':Title}
	return render(request,'download.html',context)


def yt_download_done(request,resolution):
	global url
	homedir=os.expanduser('~')
	dirs=homedir+'/Downloads'
	if request.method=="POST":
		YouTube(url).streams.get_by_resolution(resolution).download(dirs)
		return render(request,"done.html")

	else:
		return render(request,"error.html")
# from django.http import HttpResponse, StreamingHttpResponse
# from pytube import YouTube

# def download(request):
#     url = request.GET.get('url')
#     yt = YouTube(url)
#     stream = yt.streams.first()
    
#     def stream_file():
#         with stream.stream_to_buffer() as buffer:
#             for chunk in iter(lambda: buffer.read(1024*1024), b''):
#                 yield chunk
    
#     response = StreamingHttpResponse(stream_file(), content_type=stream.mime_type)
#     response['Content-Disposition'] = f'attachment; filename="{yt.title}.{stream.subtype}"'
#     response['Content-Length'] = stream.filesize
    
#     return response
