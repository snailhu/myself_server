#coding:utf-8
#from captcha.helpers import captcha_image_url
#from captcha.models import CaptchaStore
from django.core.context_processors import csrf
from django.http import HttpResponse

from django.shortcuts import render, render_to_response
import uuid
# Create your views here.
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt, csrf_protect
#from MyselfApp.forms import CaptchaTestForm
#
#@csrf_exempt
##@csrf_protect
#def some_view(request):
#    if request.POST:
#        form = CaptchaTestForm(request.POST)
#
#        # Validate the form: the captcha field will automatically
#        # check the input
#        if form.is_valid():
#            human = True
#    else:
#        form = CaptchaTestForm()
#    return render_to_response('template.html', {'form':form})
#
##@csrf_exempt
#def refresh(request):
#   if request.GET.get('newsn')=='1':
#        csn=CaptchaStore.generate_key()
#        cimageurl = captcha_image_url(csn)
#        return HttpResponse(cimageurl)
#FILE_PATH = '/root/red5-1.0.0/webapps/oflaDemo/streams/'
@csrf_exempt
def index(request):
     return render_to_response('index.html')

FILE_PATH = '/root/red5/webapps/oflaDemo/streams/'
RTMP_PATH = 'rtmp://192.168.1.165/oflaDemo'
@csrf_exempt
def upload_file(request):
    file = request.FILES.get('upload_file',None)
    if file:
        type = file.name.split('.')[-1]
        uuid_string = str(uuid.uuid1())
        file_name = uuid_string + '.'+type+''
        file_path = FILE_PATH + file_name
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
            destination.close()
        return render_to_response('play.html', {'filepath': file_name, 'rtmp_path': RTMP_PATH})

def player(request):
    return render_to_response('play.html')
