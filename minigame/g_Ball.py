#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-09 11:09:23
# @Author  : FILVZ (497230472@qq.com)
# @Link    : 
# @Version : $Id$

import pygame
class ball():
    def __init__(self, screen,m_balck):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("e:\\git\python\\Alien invasion\\images\\ball.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = m_balck.rect.top - 2
        self.moveing = False
        self.offsetX = 1
        self.offsetY = 1
        self.center_X=self.rect.centerx
        self.center_Y=self.rect.centery
    def blitme(self):
        """在指定位置绘制球"""
        self.screen.blit(self.image, self.rect)
    def move(self,rect,ai_settings):
        set=ai_settings
        if self.offsetX>0:
            self.offsetX = set.ball_speed
        else:
            self.offsetX = -set.ball_speed
        if self.offsetY>0:
            self.offsetY = set.ball_speed
        else:
            self.offsetY = -set.ball_speed
        if self.moveing:
            # if 0 <= self.rect.top - rect.bottom <0.1 and \
            #         ((self.rect.left > rect.left and self.rect.right < rect.right) or
            #              (self.rect.left > rect.left and self.rect.right - rect.right < self.rect.w) or
            #              (self.rect.left < rect.left and rect.left - self.rect.left < self.rect.w)):
            #     self.offsetY *= -1
            #     print('self.rect.top - rect.bottom')
            # if -0.1 < self.rect.bottom - rect.top <=0 and \
            #         ((self.rect.left > rect.left and self.rect.right < rect.right) or
            #              (self.rect.left > rect.left and self.rect.right - rect.right< self.rect.w) or
            #              (self.rect.left < rect.left and rect.left - self.rect.left < self.rect.w)):
            #     self.offsetY *= -1
            #     print('self.rect.bottom - rect.top')
            # if 0 <= self.rect.right - rect.left <0.1 and \
            #         ((self.rect.top <= rect.top and self.rect.bottom >= rect.bottom) or
            #              (self.rect.top<= rect.top and 0 <= rect.bottom - self.rect.bottom < rect.h) or
            #              (self.rect.top>= rect.top and self.rect.bottom - rect.bottom < self.rect.h)):
            #     self.offsetX *= -1
            #     print('self.rect.right - rect.left')
            # if 0 <= self.rect.left - rect.right <0.1 and \
            #         ((self.rect.top <= rect.top and self.rect.bottom >= rect.bottom) or
            #              (self.rect.top<= rect.top and 0 <= rect.bottom - self.rect.bottom < rect.h) or
            #              (self.rect.top>= rect.top and self.rect.bottom - rect.bottom < self.rect.h)):
            #     self.offsetX *= -1
            #     print('self.rect.left - rect.right')

            if self.rect.left - self.offsetX < 0:
                self.offsetX *= -1
                print('left')
            elif self.rect.right - self.offsetX > self.screen_rect.right:
                self.offsetX *= -1
                print('right')
            if self.rect.top - self.offsetY <  0:
                self.offsetY *= -1
                print('top')
            elif self.rect.bottom - self.offsetY > self.screen_rect.bottom :
                self.offsetY *= -1
                print('bottom')

            self.center_X -= self.offsetX
            self.center_Y -= self.offsetY

            self.rect.centerx = self.center_X
            self.rect.centery = self.center_Y
    def move(self):
            if self.rect.left - self.offsetX < 0:
                self.offsetX *= -1
                print('left')
            elif self.rect.right - self.offsetX > self.screen_rect.right:
                self.offsetX *= -1
                print('right')
            if self.rect.top - self.offsetY <  0:
                self.offsetY *= -1
                print('top')
            elif self.rect.bottom - self.offsetY > self.screen_rect.bottom :
                self.offsetY *= -1
                print('bottom')

            self.center_X -= self.offsetX
            self.center_Y -= self.offsetY

            self.rect.centerx = self.center_X
            self.rect.centery = self.center_Y


