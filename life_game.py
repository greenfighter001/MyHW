import game_map
from UI import UI

row = 30
col = 30
ratio = 0.5

class LifeGame:
    def __init__(self, map_rows, map_cols, life_init_ratio):
        """将在主程序中初始化实例"""
        Map = UI(game_map.GameMap(row, col))

    def game_cycle(self):
        """进行一次游戏循环，将在此完成地图的更新，将在计时器触发时被调用"""
        pass

if __name__ == '__main__':
    lifeGame = LifeGame(row, col, ratio)
