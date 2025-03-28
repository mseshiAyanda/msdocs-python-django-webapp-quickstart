from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from videoapp.camera import VideoCamera
# Create your views here.
def index(request):
    return render(request, 'videoapp/index.html')
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def video_stream(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                    content_type='multipart/x-mixed-replace; boundary=frame')
