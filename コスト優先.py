import copy
dx=[1,0,-1,0]
dy=[0,-1,0,1]

def yokotansaku(h,w,t):
  y,x=[0,0]
  gy,gx=[h-1,w-1]
  cost=0
  que=[]
  his=[]
  his.append([-1,-1])
  que.append([0,0,0,his])
  while len(que)>0:
    y,x,cost,his  = que.pop()
    if y==gy and x==gx:
      return cost
    if ([y,x] in his)==True:
      continue
    his.append([y,x])
    for i in range(0,4):
      ny = y + dy[i]
      nx = x + dx[i]
      if ny < 0 or ny >= h or nx < 0 or nx >= w:
        continue
      else:
        ncost = cost + int(t[ny][nx])
        que.append([ny,nx,ncost,his])
    que = sorted(que,reverse=True,key=lambda x:x[2])

h,w = map(int,input().split())
t=[]
for i in range(h):
  line = input().split()
  t.append(line)

print(yokotansaku(h,w,t))
