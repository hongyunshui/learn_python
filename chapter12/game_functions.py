#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-03-17 22:09
# @Author  : hys
# @Site    : 
# @File    : game_functions.py
# @Software: PyCharm
# @Desc     :
# @license : Copyright(C), Your Company
# @Contact : george.zw513@gmail.com
import sys
import pygame
from chapter12.bullet import Bullet
from chapter12.alien import Alien
from time import sleep


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键
    :param event: 中断事件对象
    :param ai_settings: 游戏参数设置对象
    :param screen: 游戏背景屏幕对象
    :param ship: 飞船对象
    :param bullets: 子弹对象
    """
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船标志位
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动飞船标志位
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        # 向上移动飞船标志位
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        # 向下移动飞船标志位
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # 响应创建子弹事件
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """响应松开事件"""
    if event.key == pygame.K_RIGHT:
        # 向右移动标志位
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 向左移动标志位
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        # 向上移动飞船标志位
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        # 向下移动飞船标志位
        ship.moving_down = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """响应按键和鼠标事件
    :param aliens:
    :param stats: 跟踪游戏信息对象
    :param play_button: 按键对象
    :param ai_settings: 游戏设置对象
    :param screen: 游戏背景屏幕对象
    :param ship: 飞船对象
    :param bullets: 子弹对象
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 响应结束程序事件
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # 响应按键事件
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            # 响应松开事件
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 响应鼠标按下事件
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """在玩家单击Play按键时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏
        ai_settings.initialize_dynamic_settings()
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重置游戏统计信息
        stats.game_active = True
        stats.reset_stats()
        # 重置记分牌
        sb.prep_score()  # 显示当前得分
        sb.prep_high_score()  # 显示最高分
        sb.prep_level()  # 显示游戏等级
        sb.prep_ships()  # 绘制剩余飞船数量
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """更新屏幕上的图像，并切换到新屏幕
    :param sb:
    :param stats:
    :param play_button:
    :param ai_settings: 游戏相关参数设置
    :param screen: 游戏背景屏幕对象
    :param ship: 飞船对象
    :param aliens: 外星人对象
    :param bullets: 子弹对象
    """
    # 每次循环时都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    # 重新绘制飞船
    ship.blitme()
    # 重新绘制外星人
    aliens.draw(screen)
    # 绘制子弹
    for bullet in bullets:
        bullet.draw_bullet()
    # 显示得分
    sb.show_score()
    # 如果游戏处于非活动状态，就显示PLAY按钮
    if not stats.game_active:
        play_button.draw_button()
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """更新子弹的位置，并删除已消失的子弹，检查是否有子弹击中了外星人，如果有就删除对应的子弹和外星人
    :param stats:
    :param sb:
    :param ai_settings:
    :param screen:
    :param ship:
    :param aliens:
    :param bullets:子弹对象
    """
    # 更新子弹位置
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 响应子弹和外星人的碰撞
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    响应子弹和外星人的碰撞
    :param stats:
    :param sb:
    :param ai_settings:游戏的参数设置对象
    :param screen:游戏背景对象
    :param ship:飞船对象
    :param aliens:外星人对象
    :param bullets:子弹对象
    """
    # 删除发生碰撞的外星人和子弹
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    # 如果有子弹击中外星人，增加得分
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()  # 跟新显示的得分
        check_high_score(stats, sb)  # 检查是否打破最高得分
    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        bullets.empty()  # 删除现有的子弹
        ai_settings.increase_speed()  # 加快游戏节奏
        # 提高等级
        stats.level += 1
        sb.prep_level()
        # 创建新的外星人
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有达到限制，就发射一颗子弹"""
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人并计算一行可以容纳多少个外星人
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # 创建外星人人群
    for row_number in range(number_rows):
        # 创建一行外星人
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可以容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少外星人"""
    availabe_space_y = (ai_settings.screen_height -
                        (3 * alien_height) - ship_height)
    number_rows = int(availabe_space_y / (2 * alien_height))
    return number_rows


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """响应外星人撞到飞船"""
    if stats.ships_left > 0:  # 如果剩余飞船数量大于0
        # 将ship_left减1
        stats.ships_left -= 1
        # 更新飞船剩余数量
        sb.prep_ships()
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人，并将飞船放到屏幕低端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """检查是否有外星人位于屏幕边缘，并更新整群外星人的位置
    :param screen:
    :param bullets:
    :param stats: 游戏信息跟踪对象
    :param ship: 飞船对象
    :param ai_settings: 游戏设置对象
    :param aliens: 外星人群对象
    """
    # 响应外星人到达边缘
    check_fleet_edges(ai_settings, aliens)
    aliens.update()  # 自动对每个外星人调用update()方法
    # 检测飞船和外星人之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
    # 检查是否有外星人到达屏幕低端
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """检查是否有外星人到达了屏幕低端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 有外星人到达底端，飞船被摧毁
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break


def check_high_score(stats, sb):
    """检查是否诞生了新的最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

