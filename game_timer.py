import pygame

class GameTimer:
    def __init__(self, interval):
        """将在主程序中初始化实例，计时器以interval秒的频率触发
        trigger是个函数，计时器被触发时调用该函数"""
        self.tick = 1/interval
        self.clock = pygame.time.Clock()

    def start(self):
        """启动计时器，之后将以interval秒的间隔持续触发"""
        self.clock.tick(self.tick)
