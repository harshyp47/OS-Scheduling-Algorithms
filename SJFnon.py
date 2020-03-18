n=int(input("Enter the number of processes:"))
processes=[]
bt=[]


for i in range(n):
    x=int(input("Enter Pid:"))
    y = int(input("Enter BurstTime "+"For p"+str(x)+":"))
    processes.append("p"+str(x))
    bt.append(y)


for i in range(0,len(bt)-1):
    for j in range(0,len(bt)-i-1):
        if(bt[j]>bt[j+1]):
            temp=bt[j]
            bt[j]=bt[j+1]
            bt[j+1]=temp
            temp=processes[j]
            processes[j]=processes[j+1]
            processes[j+1]=temp
wt=[]
avgwt=0
tat=[]
avgtat=0
wt.insert(0,0)
tat.insert(0,bt[0])
for i in range(1,len(bt)):
    wt.insert(i,wt[i-1]+bt[i-1])
    tat.insert(i,wt[i]+bt[i])
    avgwt+=wt[i]
    avgtat+=tat[i]
    avgwt=float(avgwt)/n
    avgtat=float(avgtat)/n

print("ProcessesArray:")
print(processes)
print("WaitingTime array:")
print(wt)
print("TurnAroundTimeArray:")
print(tat)
print("AverageWaitingTime:")
print(avgwt)
print("AverageTurnAroundTime:")
print(avgtat)
