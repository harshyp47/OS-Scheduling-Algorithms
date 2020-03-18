def WaitingTime(pid,burst,atime,n,wt):
    for i in burst:
        rt.append(i)
    complete=0
    t=0
    minm=999999999
    short=0
    check=False

    while(complete!=n):
        for j in range(n):
            if ((atime[j]<=t) and (rt[j]<minm) and rt[j]>0):
                minm=rt[j]
                short=j
                check=True
        if(check==False):
            t=t+1
            continue

        rt[short]=rt[short]-1
        minm=rt[short]
        if(minm==0):
            minm=999999999

        if(rt[short]==0):
            complete=complete+1
            check=False
            fint=t+1
            wt[short]=(fint-burst[short]-atime[short])
            if(wt[short]<0):
                wt[short]=0
        t=t+1

def TAT(pid,burst,atime,n,wt,tat):
    for i in range(n):
        tat[i]=burst[i]+wt[i]

def AVGT(pid,burst,atime,n):
    wt=[]
    tat=[]
    for i in range(n):
        wt.append(0)
        tat.append(0)

    WaitingTime(pid,burst,atime,n,wt)
    TAT(pid,burst,atime,n,wt,tat)
    totalwt=0
    totaltat=0
    for i in range(n):
        totalwt=totalwt+wt[i]
        totaltat=totaltat+tat[i]
    print("ProcessesArray:")
    print(pid)
    print("WaitingTime array:")
    print(wt)
    print("TurnAroundTimeArray:")
    print(tat)
    print("AverageWaitingTime:")
    print(totalwt/n)
    print("AverageTurnAroundTime:")
    print(totaltat/n)

n=int(input("Enter the number of processes:"))
pid=[]
burst=[]
atime=[]
rt=[]
for i in range(n):
    x=int(input("Enter Pid:"))
    y = int(input("Enter BurstTime "+"For p"+str(x)+":"))
    z = int(input("Enter ArrivalTime "+"For p"+str(x)+":"))
    pid.append("p"+str(x))
    burst.append(y)
    atime.append(z)
AVGT(pid,burst,atime,n)