#問題1: 幅優先探索 - 迷路 Python3編

import copy
dx=[1,0,-1,0]
dy=[0,-1,0,1]
muki={'R':0,'U':1,'L':2,'D':3}

def yokotansaku(h,w,t):
    y,x=[0,0]
    gy,gx=[h-1,w-1]
    cost=1
    que=[]
    que.append([0,0])
    closeque=[]
    while True:
        #print(cost,que)
        tmpquq=[]
        while len(que)>0:
            y,x = que.pop()
            if y==gy and x==gx:
                t[y][x]='9'
                return cost
            if t[y][x] == '1':
                continue
            if closeque.count([y,x])>0:
                continue
            closeque.append([y,x])
            t[y][x]='9'
            for i in range(0,4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= h or nx < 0 or nx >= w:
                    continue
                else:
                    tmpquq.append([ny,nx])
        que = tmpquq.copy()
        cost+=1

h,w = map(int,input().split())
t=[]
for i in range(h):
    line = input().split()
    t.append(line)


print(yokotansaku(h,w,t))

#for i in range(h):
#    print(t[i])
