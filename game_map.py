import random

class GameMap:
    def __init__(self, rows, cols):
        """地图将在逻辑模块进行初始化"""
        self.Row = rows
        self.Col = cols
        self.map = [[False for _ in range(cols)] for _ in range(rows)]
        self.life_ratio = 0.5
        self.reset(rows, cols, self.life_ratio)

    def reset(self, rows, cols, life_ratio):
        """重置地图并按life_ratio随机地填充一些活细胞"""
        for i in range(rows):
            for j in range(cols):
                if random.random() <= life_ratio:
                    self.set(i, j, True)
                else:
                    self.set(i, j, False)

    def get_neighbor_count(self, row, col):
        """地图上一个方格周围或细胞数是游戏逻辑里的重要数据"""
        count = 0
        bias = [(1, 0), (1, -1), (0, -1), (-1, -1),
                (-1, 0), (-1, 1), (0, 1), (1, 1)]
        for i, j in bias:
            if 0 <= row + i < self.Row and 0 <= col + j < self.Col:
                count += int(self.get(row+i, col+j))
        return count

    def set(self, row, col, val):
        """当游戏进行中，需要常常更新地图上的方格的状态"""
        self.map[row][col] = val

    def get(self, row, col):
        """当需要将游戏状态呈现给用户时，就需要获取地图上方格的状态"""
        return self.map[row][col]

    def update(self, rows, cols):
        count = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                count[i][j] = self.get_neighbor_count(i, j)
        for i in range(rows):
            for j in range(cols):
                if count[i][j] > 3 or count[i][j] < 2:
                    self.set(i, j, False)
                elif count[i][j] == 3:
                    self.set(i, j, True)
