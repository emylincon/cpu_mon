import psutil
import time
import os

cpu = []


def get_cpu():
    global cpu
    prev_t = 0
    next_t = psutil.cpu_percent(percpu=False)
    delta = abs(prev_t - next_t)
    prev_t = next_t
    cpu.append(delta)
    #os.system('echo "{}," >> cpu_log.txt'.format(delta))
    time.sleep(1)
    print('cpu', delta)


def main():
    while True:
        try:
            get_cpu()
        except:
            print(cpu)
            os.system('echo "{}" >> cpu_log.txt'.format(cpu))
            break


main()
