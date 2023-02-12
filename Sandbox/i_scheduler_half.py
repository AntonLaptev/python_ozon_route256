import bisect
p,z=list(map(int, input().split()))
proc_status = [[0]*2 for i in range(p)]
#print(proc_status)
proc=list(map(int, input().split()))
#print(proc)

for i in range(p):
    proc_status[i][1]=  proc[i]
#print(proc_status)


m=0
for j in range(z):
    task_beg_time,task_execution_time=list(map(int, input().split()))
    task_end_time=task_beg_time+task_execution_time
    #print(task_beg_time,task_execution_time,task_end_time)
    if min(list(map(list, zip(*proc_status)))[0])<=task_beg_time:
        proc_status.sort(key = lambda x: x[0])
        #print(proc_status)
        #print(list(map(list, zip(*proc_status)))[0])
        index = bisect.bisect(list(map(list, zip(*proc_status)))[0], task_beg_time)
        #print(index)
        #print(proc_status[:index])
        #now_spis=proc_status[:index]
        min_proc=min(list(map(list, zip(*proc_status[:index])))[1])
        #print(min_proc)
        #spis_2=list(map(list, zip(*proc_status[:index])))[1]
        #print(list(map(list, zip(*proc_status[:index])))[1])
        num_min_proc=list(map(list, zip(*proc_status[:index])))[1].index(min_proc)
        #print(num_min_proc)
        #print(proc_status[num_min_proc][0])
        proc_status[num_min_proc][0]=task_end_time
        #print(proc_status[num_min_proc][0])
        m+=task_execution_time*min_proc
        #print(task_end_time)
        #print(proc_status)
print(m)

