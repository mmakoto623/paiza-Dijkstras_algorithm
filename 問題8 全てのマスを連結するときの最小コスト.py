
import heapq

class State:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost

    def __lt__(self, state):
        return self.cost < state.cost
        
    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, state):
        return self.x == state.x and \
            self.y == state.y

def dijkstra(sy,sx,gy,gx):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    cost=0
    openque = []
    closedque = set()
    state = State(sx, sy, 0)
    heapq.heappush(openque, state)
    while len(openque) > 0:
        state = heapq.heappop(openque)
        if state in closedque:
            continue
        closedque.add(state)
        cost += state.cost
        if (len(closedque) == w * h):
            return cost;
        for i in range(4):
            nx = state.x + dx[i]
            ny = state.y + dy[i]
            if nx < 0 or w <= nx or ny < 0 or h <= ny:
                continue
            ncost = t[state.y][state.x] * (t[ny][nx])
            heapq.heappush(openque, State(nx, ny, ncost))

h, w = map(int, input().split())
t= [list(map(int,input().split())) for i in range(h)]

print( dijkstra(0,0,h-1,w-1) )
