#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-07 19:14:20
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
		# self.rect.centery = self.screen_rect.centery
		self.rect.bottom = self.screen_rect.bottom
		self.offset=3
		self.moveLeft=False
		self.moveRight=False
		self.moveUp=False
		self.moveDown=False
		self.centerX=self.rect.centerx
		self.centerY=self.rect.centery
	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image, self.rect)
	def move(self):
		if self.moveLeft and self.rect.left > 0:
			self.centerX -= self.offset
		elif self.moveRight and self.rect.right < self.screen_rect.right:
			self.centerX += self.offset
		if self.moveUp and self.rect.top > 0:
			self.centerY -= self.offset
		elif self.moveDown and self.rect.bottom < self.screen_rect.bottom:
			self.centerY += self.offset

		self.rect.centerx = self.centerX
		self.rect.centery = self.centerY
