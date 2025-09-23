import sys
import heapq

tc=int(sys.stdin.readline())

for _ in range(tc):
    n=int(sys.stdin.readline())

    isDeleted=[False]*n

    minHeap = []
    maxHeap = []

    for i in range(n):

        cmd,target=sys.stdin.readline().rstrip().split()
        target=int(target)

        if cmd=='I':
            heapq.heappush(minHeap,(target,i))
            heapq.heappush(maxHeap,(-target,i))
        else:
            if target==1:
                while maxHeap and isDeleted[maxHeap[0][1]]:
                    heapq.heappop(maxHeap)
                if maxHeap:
                    number,key=heapq.heappop(maxHeap)
                    isDeleted[key]=True
            else:
                while minHeap and isDeleted[minHeap[0][1]]:
                    heapq.heappop(minHeap)

                if minHeap:
                    number,key=heapq.heappop(minHeap)
                    isDeleted[key] = True

    while maxHeap and isDeleted[maxHeap[0][1]]:
        heapq.heappop(maxHeap)
    while minHeap and isDeleted[minHeap[0][1]]:
        heapq.heappop(minHeap)

    if not minHeap:
        print("EMPTY")
    else:
        print(-maxHeap[0][0],minHeap[0][0]) 