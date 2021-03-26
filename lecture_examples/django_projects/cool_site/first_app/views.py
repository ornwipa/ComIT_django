from django.shortcuts import render

# Create your views here.

from django.template.response import SimpleTemplateResponse
from datetime import datetime

def get_current_time(request):
	current_time = datetime.now()
    time_zone = request.GET.get('time_zone', None)

	# html = f"<html><body>It is now {current_time} in {time_zone}.</body></html>"
    # return HttpResponse(html)

    the_data = {
        'current_time': current_time,
        'time_zone': time_zone
    }
    return SimpleTemplateResponse('current_time.html', the_data)

def hello_world(request, **kwargs): # add arguments to take variables from URL
    current_time = datetime.now()

    # return HttpResponse("Hello")
    
    the_data = {
        'current_time': current_time,
        'name': name,
        'number': number
    }
    return SimpleTemplateResponse('current_time.html', the_data)
