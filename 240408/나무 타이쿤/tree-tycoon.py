n,y = map(int, input().split())
graph = []
moves = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
for _ in range(y):
    moves.append(list(map(int, input().split())))

def move_it(state, direction):
    temp_c = state[1]
    temp_r = state[0]
    for i in range(direction[1]):
        if direction[0] == 1:
            temp_c += 1
            if temp_c == n:
                temp_c = 0
        if direction[0] == 2:
            temp_c += 1
            temp_r -= 1
            if temp_c == n:
                temp_c = 0
            if temp_r == -1:
                temp_r = n-1
        if direction[0] == 3:
            temp_r -= 1
            if temp_r == -1:
                temp_r = n-1
        if direction[0] == 4:
            temp_c -= 1
            temp_r -= 1
            if temp_c == -1:
                temp_c = n-1
            if temp_r == -1:
                temp_r = n-1
        if direction[0] == 5:
            temp_c -= 1
            if temp_c == -1:
                temp_c = n-1
        if direction[0] == 6:
            temp_c -= 1
            temp_r += 1
            if temp_c == -1:
                temp_c = n-1
            if temp_r == n:
                temp_r = 0
        if direction[0] == 7:
            temp_r += 1
            if temp_r == n:
                temp_r = 0
        if direction[0] == 8:
            temp_c += 1
            temp_r += 1
            if temp_c == n:
                temp_c = 0
            if temp_r == n:
                temp_r = 0
    return [temp_r, temp_c]

dr = [-1, -1, 1, 1]
dc = [-1,  1, -1, 1]

def append_libro(state):
    total_plus = 0
    temp_r = state[0]
    temp_c = state[1]

    for i in range(4):
        temp_temp_c = temp_c + dc[i]
        temp_temp_r = temp_r + dr[i]
        if 0 <= temp_temp_c < n and 0 <= temp_temp_r < n:
            if graph[temp_temp_r][temp_temp_c] >= 1:
                total_plus += 1
    return total_plus

libros = [[n-2, 0, graph[n-2][0]], [n-2, 1, graph[n-2][1]], [n-1, 0, graph[n-1][0]], [n-1, 1, graph[n-1][1]]]

for move in moves:
    moved_libros = []
    for libro in libros:
        moved_libros.append(move_it(libro, move)) # r, c
    for moved_libro in moved_libros:
        graph[moved_libro[0]][moved_libro[1]] += 1
    
    plus_list = []
    for moved_libro in moved_libros:
        plus_value = append_libro(moved_libro)
        plus_list.append([moved_libro[0], moved_libro[1], plus_value])
    
    for plus_cluster in plus_list:
        graph[plus_cluster[0]][plus_cluster[1]] += plus_cluster[2]
    libros = []

    for r in range(n):
        for c in range(n):
            if [r, c] not in moved_libros:
                if graph[r][c] >= 2:
                    graph[r][c] -= 2
                    libros.append([r, c, graph[r][c]])

count = 0
for r in range(n):
    for c in range(n):
        count += graph[r][c]

print(count)