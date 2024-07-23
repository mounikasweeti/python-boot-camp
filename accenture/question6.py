#n=int(input())
#arr=list(map(int,input().split(" ")))
#counter={}
#for i in arr:
 #   if i in counter:
  #      counter[i]+=1
   # else:
    #    counter[i]=1
#print(*counter.items())
#ans,maxValue=0,0
#for key,value in counter.items():
 #   if value>maxValue:
  #      maxValue=key
   #     ans=key
#print(ans)
n = 10
arr = [9,9,9,3,3,3,1,1,1,5]
counter = {}
for i in arr:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1
newArray = list(counter.items())
newArray.sort(key = lambda ele: ele[1])
print(newArray)
if newArray[-1]>newArray[-2]:
    print(newArray[-1])
else:
    print(-1)
