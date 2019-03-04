from django.http import HttpResponse
import psutil
import time


def mon(request):
    return HttpResponse("Start to monitor...")


def list_process(request):
    pids = psutil.pids()
    process_list = [];
    for pid in pids:
        process = psutil.Process(pid)
        process_list.append(process)
    # result = "\n".join("pid:{} name:{}".format(x.pid, x.name()) for x in process_list)
    result = "\n".join(str(x) for x in process_list)
    return HttpResponse("Start to monitor internal:%s " % result)


def mon_process(request, internal, count, process_id):
    curr_time = time.strftime('%Y-%m-%d-%H-%M-%S')
    file = open("monitor%s-%s.csv" % (process_id, curr_time), "w")
    cpu_count = psutil.cpu_count()
    cpu_array = []
    j = 0
    while j < cpu_count:
        cpu_array.append("cpu{}".format(str(j)))
        j = j+1
    csv_head_cpu = " ".join(str(x) for x in cpu_array)
    file.write("{} {} {}\n".format(curr_time, csv_head_cpu, " vmfree vmpercent vmavailable vmtotal"))
    file.flush()
    i = 0
    while i < count:
        curr_time = time.strftime('%Y-%m-%d-%H:%M:%S')
        cpu_stats = psutil.cpu_percent(internal, percpu=True)
        virtual_mem_stats = psutil.virtual_memory()
        # file.write("%s %s %f %f %f %f \n" % (curr_time,cpu_stats, virtual_mem_stats.free, virtual_mem_stats.percent, virtual_mem_stats.available, virtual_mem_stats.total))
        cpu = " ".join(str(x) for x in cpu_stats)
        file.write("{} {} {:.0f} {:.2f} {:.0f} {:.0f}\n".format(curr_time, cpu, virtual_mem_stats.free, virtual_mem_stats.percent, virtual_mem_stats.available, virtual_mem_stats.total))
        file.flush()
        i = i+1
    file.close()
    return HttpResponse("Start to monitor internal:%s seconds count:%s process: %s...." % (internal, count, process_id))


def mon_sys(request, internal, count):
    curr_time = time.strftime('%Y-%m-%d-%H-%M-%S')
    file = open("monitor%s.csv" % curr_time, "w")
    cpu_count = psutil.cpu_count()
    cpu_array = []
    j = 0
    while j < cpu_count:
        cpu_array.append("cpu{}".format(str(j)))
        j = j+1
    csv_head_cpu = " ".join(str(x) for x in cpu_array)
    file.write("{} {} {}\n".format(curr_time, csv_head_cpu, " vmfree vmpercent vmavailable vmtotal"))
    file.flush()
    i = 0
    while i < count:
        curr_time = time.strftime('%Y-%m-%d-%H:%M:%S')
        cpu_stats = psutil.cpu_percent(internal, percpu=True)
        virtual_mem_stats = psutil.virtual_memory()
        cpu = " ".join(str(x) for x in cpu_stats)
        file.write("{} {} {:.0f} {:.2f} {:.0f} {:.0f}\n".format(curr_time, cpu, virtual_mem_stats.free, virtual_mem_stats.percent, virtual_mem_stats.available, virtual_mem_stats.total))
        file.flush()
        i = i+1
    file.close()
    return HttpResponse("Start to monitor internal:%s seconds count:%s ...." % (internal, count))
