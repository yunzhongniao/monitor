from django.http import HttpResponse
from django.template import loader
import psutil


def index(request):
    template = loader.get_template('monitor/index.html')
    pid_list = psutil.pids()
    process_list = [];
    for pid in pid_list:
        process = psutil.Process(pid)
        process_list.append(process)
    context = {
        'hello': 'Hello Index',
        'processes': process_list
    }
    return HttpResponse(template.render(context, request))


def process_view(request, process_id):
    process = psutil.Process(process_id)
    context = {
        "process": process,
        "pid": process_id
    }
    template = loader.get_template('monitor/process_view.html')
    return HttpResponse(template.render(context, request))
