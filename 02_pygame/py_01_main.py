"""
需要切换系统解释器,方可使用/usr/local/lib下的pygame
"""
import pygame

pygame.init()

print(pygame.__file__)
hero_rect = pygame.Rect(100, 200, 300, 400)  # x,y,width,height
print("x:%d, y:%d" % (hero_rect.x, hero_rect.y))
print("width:%d,height:%d" % (hero_rect.width, hero_rect.height))
print("%d,%D" % hero_rect.size)  # size是个元组

pygame.quit()
