while True:
    try:
        m, n = list(map(int, input().split()))
        maze = []
        for _ in range(m):
            maze.append(list(map(int, input().split())))


        def walk(i, j, pos=[(0, 0)]):
            if j + 1 < n and maze[i][j + 1] == 0:  # 向右
                if (i, j + 1) not in pos:
                    walk(i, j + 1, pos + [(i, j + 1)])
            if j - 1 >= 0 and maze[i][j - 1] == 0:  # 向左
                if (i, j - 1) not in pos:
                    walk(i, j - 1, pos + [(i, j - 1)])
            if i + 1 < m and maze[i + 1][j] == 0:  # 向下
                if (i + 1, j) not in pos:
                    walk(i + 1, j, pos + [(i + 1, j)])
            if i - 1 >= 0 and maze[i - 1][j] == 0:  # 向上
                if (i - 1, j) not in pos:
                    walk(i - 1, j, pos + [(i - 1, j)])
            if (i, j) == (m - 1, n - 1):  # 到达出口
                for p in pos:
                    print('(' + str(p[0]) + ',' + str(p[1]) + ')')


        walk(0, 0)
    except:
        break
