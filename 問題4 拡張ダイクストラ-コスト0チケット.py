import heapq

class State:
    def __init__(self, x, y, n,cost):
        self.x = x
        self.y = y
        self.ticket= n
        self.cost = cost

    def __lt__(self, state):
        return self.cost < state.cost
        
    def __hash__(self):
        return hash((self.x, self.y, self.cost, self.ticket))

    def __eq__(self, state):
        return self.x == state.x and \
            self.y == state.y and \
            self.cost == state.cost and \
            self.ticket == state.ticket

def dijkstra():
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    sy=0
    sx=0
    gy=h-1
    gx=w-1
    openque = []
    closedque = set()
    state = State(sx, sy, n,t[sy][sx])
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
            heapq.heappush(openque, State(nx, ny, state.ticket ,ncost))
            if state.ticket >0:
                heapq.heappush(openque, State(nx, ny, state.ticket-1 ,state.cost))
            
h, w = map(int, input().split())
t= [list(map(int,input().split())) for i in range(h)]
n = int(input())

print(dijkstra())
