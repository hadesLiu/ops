
import psutil as psutil

# cpu

# print psutil.cpu_times()
# print psutil.cpu_times().user
# print psutil.cpu_times(percpu=True)
#
# print psutil.cpu_count()
# print psutil.cpu_count(logical=False)

# memory

# mem = psutil.virtual_memory()
# print mem
# print mem.total, mem.available, mem.used
#
# print psutil.swap_memory()

# disk

# print psutil.disk_partitions()
#
# print psutil.disk_usage('/')
#
# print psutil.disk_io_counters()
# print psutil.disk_io_counters(perdisk=True)

# network

# print psutil.net_io_counters()
# print psutil.net_io_counters(pernic=True)

# others

# import datetime
# print psutil.users()
# print psutil.boot_time()
# print datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H: %M: %S')

# process info

# print psutil.pids()

# process info: class Process

# p = psutil.Process(78540)
# print p.name()
# print p.exe()
# print p.cwd()
# print p.status()
# print p.create_time()
# print p.uids()
# print p.gids()
# print p.cpu_times()
# print p.cpu_affinity()
# print p.memory_percent()
# print p.memory_info()
# print p.io_counters()
# print p.connections()
# print p.num_threads()

# process info: class Popen

# from subprocess import PIPE
#
# p = psutil.Popen(["/usr/bin/python", "-c", "print('hello')"], stdout=PIPE)
# print p.name()
# print p.username()
# print p.cpu_times()
# print p.communicate()




