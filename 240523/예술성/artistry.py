import itertools
from collections import deque
N = int(input())
board = []
answer = 0
for _ in range(N):
    board.append(list(map(int, input().split())))
init_table_board = []
visited = [[False for _ in range(N)] for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(start):
    # nonlocal init_table_board
    bag = [start]
    queue = deque()
    queue.append(start)

    while queue:
        popped = queue.popleft()
        for i in range(4):
            n_r = popped[0] + dr[i]
            n_c = popped[1] + dc[i]

            if 0 <= n_c < N and 0 <= n_r < N:
                if visited[n_r][n_c] == False and board[popped[0]][popped[1]] == board[n_r][n_c]:
                    visited[n_r][n_c] = True
                    bag.append((n_r, n_c))
                    queue.append((n_r, n_c))
    return bag

for i in range(4):
    visited = [[False for _ in range(N)] for _ in range(N)] # 초기화하기
    init_table_board = []
    temp_arr = [ [0] * N for _ in range(N) ] # 배열 회전하기 위해 만든 빈 배열
    half = N // 2

    # 여기서 회전하기
    if i != 0: # 첫번째는 그냥 바로 밑으로 뛰어버리기
        # 십자가 만들어버리기
        for c in range(N):
            for r in range(N):
                if c == half:
                    temp_arr[c][r] = board[r][c]
                if r == half:
                    temp_arr[c][r] = board[N - r - 1][N - c - 1]


        def square_rotate(x, y, l):  # 정사각형 모양 시계 방향 회전

            for i in range(x, x + l):
                for j in range(y, y + l):
                    ox, oy = i - x, j - y  # (0, 0)으로 변환

                    rx, ry = oy, l - ox - 1  # 시계 방향 회전 공식

                    temp_arr[rx + x][ry + y] = board[i][j]  # 모든 좌표에 적용할 수 있도록 인자(x, y)를 더해줌.

        square_rotate(0, 0, half)
        square_rotate(0, half + 1, half)
        square_rotate(half + 1, 0, half)
        square_rotate(half + 1, half + 1, half)
        board = temp_arr
    # init_table 채우기!..

    for c in range(N):
        for r in range(N):
            if visited[r][c] == False:
                visited[r][c] = True
                init_table_board.append(BFS((r, c)))

    arr = [i for i in range(len(init_table_board))]
    set_list = list(itertools.combinations(arr, 2))
    sector_list = []
    for com in set_list:
        if len(init_table_board[com[0]]) != 0 and len(init_table_board[com[1]]): # 둘 다 갯수가 있을때! 인접해있을 때!
            chap_num = 0 # 맞붙어있는 변의 갯수
            first_list = init_table_board[com[0]]
            second_list = init_table_board[com[1]]

            for fr in first_list: # (r, c)
                for sec in second_list:
                    if ((abs(fr[0] - sec[0]) == 1) and fr[1] == sec[1] ) or ((abs(fr[1] - sec[1]) == 1) and fr[0] == sec[0]): # 서로 맞닿아있다면?
                        chap_num += 1
            sector_list.append((len(init_table_board[com[0]]), len(init_table_board[com[1]]), chap_num, board[init_table_board[com[0]][0][0]][init_table_board[com[0]][0][1]], board[init_table_board[com[1]][0][0]][init_table_board[com[1]][0][1]])) # A의 갯수, B의 갯수, 맞닿은 갯수, A의 값 , B의 값
    for sector in sector_list:
        answer += (sector[0] + sector[1]) * sector[3] * sector[4] * sector[2]
print(answer)