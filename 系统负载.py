'''
cpu\mem\负载情况

'''
loadavg={}
def load_stat():
    f=open('/proc/loadavg')
    con=f.read().split()
    f.close()
    loadavg['lavg_1']=con[0]
    loadavg['lavg_5']=con[1]
    loadavg['lavg_15']=con[2]
    return loadavg

load_stat()
print(loadavg)

'''
mem
'''
with open('/proc/meminfo') as meminfo
    for i in meminfo:
        if i .startswith('MemTotal'):
            total_mem=i.split()
            total_mem=total_mem[1]
            continue

        elif i.startswith('MemAvailable'):
            free_mem=i.split()
            free_mem=free_mem[1]
            continue

        elif i.startswith('Buffers'):
            buff_mem=i.split()
            buff_mem-=buff_mem[1]

        elif i.startswith('Cached'):
            cache_mem=i.split()
            cache_mem=cache_mem[1]
            break
        else:
            pass
print('total_mem:'+total_mem)
