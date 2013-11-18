import psutil

from multiprocessing import Process, Value, Array


class MemoryMonitor(Process):

    def __init__(self, filter, rss=0, vrt=0, *args, **kwargs):
        self.rss = Value('i', rss)
        self.vrt = Value('i', rss)
        self.filter = Array('c', filter)
        Process.__init__(self, *args, **kwargs)

    def get_memory(self, name):
        rss_sum = 0
        vrt_sum = 0
        count = 0
        for process in psutil.process_iter():
            try:
                if name not in ' '.join(process.cmdline):
                    continue
                rss, vrt = process.get_memory_info()
            except psutil.NoSuchProcess:
                continue
            rss_sum += rss
            vrt_sum += vrt
            count += 1
        if count == 0:
            return (0, 0)
        return (rss_sum / count, vrt_sum / count)

    def run(self):
        while True:
            rss, vrt = self.get_memory(self.filter.value)
            if rss > self.rss.value:
                self.rss.value = rss
            if vrt > self.vrt.value:
                self.vrt.value = vrt

    def get_memory_values(self):
        return self.rss.value, self.vrt.value

    def reset_values(self):
        self.rss.value = self.vrt.value = 0
