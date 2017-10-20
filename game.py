#!/usr/bin/env pythonk
# -*- coding: utf-8 -*-
# @Date    : 2017-10-07 18:28:23
# @Author  : FILVZ (497230472@qq.com)
# @Link    : 
# @Version : $Id$
import os
import sys
import pygame
from settings import settings
from black import block
from g_Ball import ball
def check_events(block,ball,ai_settings):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        # if event.key == pygame.K_PAGEUP:
        #     ai_settings.ball_speed += 0.001
        # elif event.key == pygame.K_PAGEDOWN:
        #     ai_settings.ball_speed -= 0.001
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_a:
                block.moveLeft=True
            elif event.key==pygame.K_d:
                block.moveRight=True
            if event.key==pygame.K_w:
                block.moveUp=True
            elif event.key==pygame.K_s:
                block.moveDown=True
            elif event.key==pygame.K_y:
                ball.moveing=True
            elif event.key==pygame.K_p:
                ball.moveing=False
        elif event.type == pygame.KEYUP:
            if event.key==pygame.K_a:
                block.moveLeft=False
            elif event.key==pygame.K_d:
                block.moveRight=False
            elif event.key==pygame.K_w:
                block.moveUp=False
            elif event.key==pygame.K_s:
                block.moveDown=False
def update_screen(ai_settings, screen, m_balck, m_ball):
    """更新屏幕上的图像， 并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 画出块
    m_balck.blitme()
    m_ball.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings =settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.game_title)
    m_balck=block(screen)
    m_balck.offset = ai_settings.block_speed
    m_ball=ball(screen,m_balck)
    m_ball.offsetX=ai_settings.ball_speed
    m_ball.offsetY=ai_settings.ball_speed
    # 开始游戏的主循环
    while  True:
        # 监视键盘和鼠标事件
        check_events(m_balck,m_ball,ai_settings)
        m_balck.move()
        # m_ball.move(m_balck.rect,ai_settings)
        m_ball.move()
        update_screen(ai_settings,screen,m_balck,m_ball)


run_game()