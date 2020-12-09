
import heapq

class State:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost

    def __lt__(self, state):
        return self.cost < state.cost
        
    def __hash__(self):
        return hash((self.x, self.y, self.cost))

    def __eq__(self, state):
        return self.x == state.x and \
            self.y == state.y and \
            self.cost == state.cost

def dijkstra(sy,sx,gy,gx):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    openque = []
    closedque = set()
    state = State(sx, sy, t[sy][sx])
    heapq.heappush(openque, state)
    while len(openque) > 0:
        state = heapq.heappop(openque)
        if state.x == gx and state.y == gy:
            return state.cost
        if state in closedque:
            continue
        closedque.add(state)

        for i in range(4):
            nx = state.x + dx[i]
            ny = state.y + dy[i]
            if nx < 0 or w <= nx or ny < 0 or h <= ny:
                continue
            ncost = state.cost + (t[ny][nx])
            heapq.heappush(openque, State(nx, ny, ncost))

            
h, w = map(int, input().split())
t= [list(map(int,input().split())) for i in range(h)]

cost1 = dijkstra(0,0,0,w-1)
cost2 = dijkstra(0,w-1,h-1,w-1)
print( cost1 + cost2 - t[0][w-1] )
