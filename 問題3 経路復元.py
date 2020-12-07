import heapq

class State:
    def __init__(self, x, y, cost, ref):
        self.x = x
        self.y = y
        self.cost = cost
        self.ref = ref

    def __lt__(self, state):
        return self.cost < state.cost

    def disp(self):
        print("--")
        for i in range(h):
            for j in range(w):
                if i == self.y and j == self.x:
                    print("*", end="")
                else:
                    print(" ", end="")
                print(t[i][j], end="")
            print("")



def dijkstra():
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    sy=0
    sx=0
    gy=h-1
    gx=w-1
    openque = []
    closedque = set()
    state = State(sx, sy, t[sy][sx], None)
    heapq.heappush(openque, state)
    while len(openque) > 0:
        state = heapq.heappop(openque)
        if state.x == gx and state.y == gy:
            return state
        if state in closedque:
            continue
        closedque.add(state)

        for i in range(4):
            nx = state.x + dx[i]
            ny = state.y + dy[i]
            if nx < 0 or w <= nx or ny < 0 or h <= ny:
                continue
            ncost = state.cost + int(t[ny][nx])
            heapq.heappush(openque, State(nx, ny, ncost, state))


h, w = map(int, input().split())
t= [list(map(int,input().split())) for i in range(h)]

st = dijkstra()
print(st.cost)
while not st == None:
    st.disp()
    st = st.ref
