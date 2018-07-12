import os
from django.shortcuts import render, render_to_response
from django.core.files.storage import FileSystemStorage
from classify_logos import reports


# Create your views here.

def index(request):
    return render_to_response('index.html',{'msg':'hello'})

def upload_image(request):
    if request.method == 'POST' and request.FILES['filename']:
        image_file = request.FILES['filename']
        fs = FileSystemStorage()
        image_path = os.path.join(os.path.curdir, "static/Data", "image.jpg")
        filename = fs.save(image_path, image_file)
        uploaded_file_url = fs.url(filename)
        result = reports.load_and_predict(uploaded_file_url)
        return render(request,'index.html', {'msg': result,'file_url': uploaded_file_url.lstrip('.')})
    else:
        return render_to_response('index.html', {'msg': ''})