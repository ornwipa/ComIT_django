from django.shortcuts import render, HttpResponse

# Create your views here.
'''
# from django.http import HttpResponse
from django.template.response import SimpleTemplateResponse
import datetime

def get_current_time(request):
	current_time = datetime.datetime.now()
    time_zone = request.GET.get('time_zone', None)
	# html = f"<html><body>It is now {current_time} in {time_zone}.</body></html>"
    # return HttpResponse(html)
    the_data = {
        'current_time': current_time,
        'time_zone': time_zone
    }
    response = SimpleTemplateResponse('current_time.html', the_data)
    return response
'''

def home(request):
    return HttpResponse("Hello")
