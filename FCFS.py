class Process:
	def __init__(self,pid,burst,alloc):
		self.pid = pid
		self.burst = burst
		self.alloc = alloc
		self.tat = None
		self.wait = None
def FCFS(pidlist):
	for i in range(len(pidlist)-1):
		for j in range(len(pidlist)-1-i):
			if(pidlist[j].alloc > pidlist[j+1].alloc ):
				pidlist[j],pidlist[j+1] = pidlist[j+1],pidlist[j]
	return pidlist

n=int(input("Enter the number of processes:"))
pid=[]
bt=[]
atime=[]
pidlist=[]


for i in range(n):
    x=int(input("Enter Pid:"))
    y = int(input("Enter BurstTime "+"For p"+str(x)+":"))
    z = int(input("Enter ArrivalTime " + "For p" + str(x) + ":"))
    pidlist.append(Process(x,y,z))

newpidlist = FCFS(pidlist)
currenttime = 0
pidnew=[]
wt=[]
tat=[]
for i in newpidlist:
    i.wait = currenttime - i.alloc
    currenttime += i.burst
    i.tat = currenttime - i.alloc
    pidnew.append(i.pid)
    tat.append(i.tat)
    wt.append(i.wait)

wttotal=0
tattotal=0
for i in range(n):
    wttotal=wttotal+wt[i]
    tattotal=tattotal+tat[i]



print("ProcessesArray:")
print(pidnew)
print("WaitingTime array:")
print(wt)
print("TurnAroundTimeArray:")
print(tat)
print("AverageWaitingTime:")
print(wttotal/n)
print("AverageTurnAroundTime:")
print(tattotal/n)
