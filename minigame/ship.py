#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-07 19:44:59
# @Author  : FILVZ (497230472@qq.com)
# @Link    : 
# @Version : $Id$

import pygame
class block():
	def __init__(self, screen):
		"""初始化飞船并设置其初始位置"""
		self.screen = screen
		# 加载飞船图像并获取其外接矩形
		self.image = pygame.image.load("e:\\git\python\\Alien invasion\\images\\balck.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		# 将每艘新飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image, self.rect)
