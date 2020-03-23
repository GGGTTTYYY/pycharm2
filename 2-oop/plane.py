# -*- coding: utf-8 -*-
import pygame
from sys import exit
from pygame.locals import *
import random

# 设置游戏屏幕大小
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800


# 子弹类
# pygame.sprite模块：pygame.sprite.Sprite为sprite模块的一个基类，Sprite类有两个成员变量：self.image 和 self.rect 还有若干成员函数 其中主要对Sprite.update
# 进行重写。Sprite类在使用时并不需要实例化，只需要继承它，然后按需写出自己的类
# 成员主要是子弹的图片对象和子弹刷出来的位置，还有移动速度。
# 一个方法就是移动，从发出位置直线往屏幕上方移动。

class Bullet():
    def __init__(self, bullet_img, init_pos):
        pygame.sprite.Sprite.__init__(self)  # 调用父类（Sprite）的构造函数
        self.image = bullet_img  # 定义实例属性：image
        self.rect = self.image.get_rect()  # 定义实例属性：rect 用该语句获得image矩形的大小 函数get_rect为获取矩阵的方法
        self.rect.midbottom = init_pos  # midbottom：矩阵操作的位置关键词，通过这段语句规定矩阵的位置
        self.speed = 10  # 定义实例属性：speed

    def move(self):
        self.rect.top -= self.speed  # self.rect.top = self.rect.top - self.speed 用减是因为rect的y坐标轴是向下为正方向，具体见图


# 玩家飞机类
# 成员变量主要是图像对象以及矩形参数和刷出位置，还会有移动速度和子弹集合（用来保存飞机射出的子弹）
class Player(pygame.sprite.Sprite):
    def __init__(self, plane_img, player_rect, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = []  # 用来存储玩家飞机图片的列表
        for i in range(len(player_rect)):
            self.image.append(plane_img.subsurface(player_rect[i]).convert_alpha())  # 用subsurface剪切读入的图片
        self.rect = player_rect[0]  # 初始化图片所在的矩形
        self.rect.topleft = init_pos  # 初始化矩形的左上角坐标
        self.speed = 8  # 初始化玩家飞机速度，这里是一个确定的值
        self.bullets = pygame.sprite.Group()  # 玩家飞机所发射的子弹的集合 当程序中有大量的实体的时候，操作这些实体将会是一件相当麻烦的事，使用精灵组将精灵放在一起
        # 统一管理，pygame使用精灵组来管理精灵的绘制和更新，精灵组是一个简单的容器
        self.is_hit = False  # 玩家是否被击中

    # 发射子弹
    def shoot(self, bullet_img):
        bullet = Bullet(bullet_img, self.rect.midtop)  # Bullet是类名 初始化变量bullet
        self.bullets.add(bullet)

    # 向上移动，需要判断边界
    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    # 向下移动，需要判断边界
    def moveDown(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed

    # 向左移动，需要判断边界
    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    # 向右移动，需要判断边界        
    def moveRight(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed


# 敌机类
# 该类保存了两个图像对象，一个是正常情况下的敌机图像。一个是爆炸的敌机图像。以便在撞击时能把撞击效果显示出来。
class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, enemy_down_imgs, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.down_imgs = enemy_down_imgs
        self.speed = 2

    # 敌机移动，边界判断及删除在游戏主循环里处理
    def move(self):
        self.rect.top += self.speed


# 初始化 pygame
pygame.init()

# 设置游戏界面大小、背景图片及标题
# 游戏界面像素大小
# pygame.display 模块控制显示窗口和屏幕
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # pygame.display.set_mode：初始化要显示的窗口和屏幕

# 游戏界面标题
pygame.display.set_caption('Python打飞机大战')  # display.set_caption：设置当前窗口标题

# 背景图
# pygame.image 用于图像传输的pygame模块
background = pygame.image.load('resources/image/background.png').convert()  # pygame.image.load 从文件中加载新图像
# 对于普通图片.convert与不加的效果一样 但可以提高blit的速度，转换格式转为像素格式

# Game Over 的背景图
game_over = pygame.image.load('resources/image/gameover.png')

# 飞机及子弹图片集合
plane_img = pygame.image.load('resources/image/shoot.png')

# 设置玩家飞机不同状态的图片列表，多张图片展示为动画效果
player_rect = []
# pygame.Rect(left, top, width, height) 用于存储直角坐标的pygame对象，left, top
# 是矩形左上点的横纵坐标，用来控制生成rect对象的位置，而后面的宽度和高度则是用来控制生成矩形的大小尺寸的，也可以传入一个object对象从而生成rect对象
player_rect.append(pygame.Rect(0, 99, 102, 126))  # 玩家飞机图片
player_rect.append(pygame.Rect(165, 234, 102, 126))  # 玩家爆炸图片

player_pos = [200, 600]
player = Player(plane_img, player_rect, player_pos)  # Player的实例化player

# 子弹图片
bullet_rect = pygame.Rect(1004, 987, 9, 21)
bullet_img = plane_img.subsurface(bullet_rect)  # 通过剪切读入子弹图片

# 敌机不同状态的图片列表，包括正常敌机，爆炸的敌机图片
enemy1_rect = pygame.Rect(534, 612, 57, 43)
enemy1_img = plane_img.subsurface(enemy1_rect)  # 通过剪切读入敌机图片
enemy1_down_imgs = plane_img.subsurface(pygame.Rect(267, 347, 57, 43))  # subsurface是Surface模块的一个方法，创建一个引用其父表面的新表面
#  使用subsurface剪切读入敌机爆炸图片

# 存储敌机，管理多个对象
enemies1 = pygame.sprite.Group()

# 存储被击毁的飞机
enemies_down = pygame.sprite.Group()

# 初始化射击及敌机移动频率
shoot_frequency = 0
enemy_frequency = 0

# 初始化分数
score = 0

# pygame.time.Clock 游戏循环帧率设置 创建一个对象来帮助跟踪时间，如果你通过可选的帧率参数，函数将延迟，以保持游戏运行速度低于给定的节拍每秒。
clock = pygame.time.Clock()

# 判断游戏循环退出的参数
running = True

# 游戏主循环
while running:

    # 这可以用来帮助限制游戏的运行速度。通过每帧调用Clock.tick(60)一次，程序的运行速度永远不会超过每秒60帧。
    clock.tick(60)

    # 生成子弹，需要控制发射频率
    # 首先判断玩家飞机没有被击中
    # shoot_frequency变量的作用就是控制子弹发射的频率，它控制在running每循环15次发射一个子弹。
    if not player.is_hit:  # 等于if player.is_hit is not False
        if shoot_frequency % 15 == 0:
            player.shoot(bullet_img)
        shoot_frequency += 1
        if shoot_frequency >= 15:
            shoot_frequency = 0

    # 生成敌机，需要控制生成频率
    # 循环50次生成一架敌机
    if enemy_frequency % 50 == 0:
        enemy1_pos = [random.randint(0, SCREEN_WIDTH - enemy1_rect.width), 0]  # 随机确定敌机的位置
        enemy1 = Enemy(enemy1_img, enemy1_down_imgs, enemy1_pos)  # Enemy类的实例化
        enemies1.add(enemy1)  # 将enemy1放在enemies1的Group里
    enemy_frequency += 1
    if enemy_frequency >= 100:
        enemy_frequency = 0

    for bullet in player.bullets:
        # 以固定速度移动子弹
        bullet.move()  # 这个bullet相当于player.bullets
        # 移动出屏幕后删除子弹
        if bullet.rect.bottom < 0:
            player.bullets.remove(bullet)

    for enemy in enemies1:
        # 2. 移动敌机
        enemy.move()
        # 3. 敌机与玩家飞机碰撞效果处理
        if pygame.sprite.collide_circle(enemy, player):  # pygame.sprite.collide_circle():通过做圆进行两个精灵之间的碰撞检测
            #  如果检测发生了碰撞
            enemies_down.add(enemy)
            enemies1.remove(enemy)
            player.is_hit = True
            break  # break跳出几层循环？应该把整个running都跳出去吧？
        # 4. 移动出屏幕后删除敌人
        if enemy.rect.top < 0:
            enemies1.remove(enemy)

    # 敌机被子弹击中效果处理
    # 将被击中的敌机对象添加到击毁敌机 Group 中
    enemies1_down = pygame.sprite.groupcollide(enemies1, player.bullets, 1, 1)
    #  pygame.sprite.groupcollide函数，这个函数是判断两个精灵组里面的精灵有没有相互碰撞的。它会把A组的精灵逐个和B组的精灵进行比较判断。
    for enemy_down in enemies1_down:
        enemies_down.add(enemy_down)

    # 绘制背景
    screen.fill(0)  # screen.fill(R,G,B),只有一个参数是什么意思？黑色？
    screen.blit(background, (0, 0))  # blit方法表示将之前的矩形区域提取并显示到screen指定的坐标位置

    # 绘制玩家飞机
    if not player.is_hit:
        screen.blit(player.image[0], player.rect)  # 将正常飞机画出来 将player.image里的正常飞机图片调出，并确定其大小和位置
    else:
        # 玩家飞机被击中后的效果处理
        screen.blit(player.image[1], player.rect)  # 将爆炸的飞机画出来
        running = False

    # 敌机被子弹击中效果显示
    for enemy_down in enemies_down:
        enemies_down.remove(enemy_down)
        score += 1
        screen.blit(enemy_down.down_imgs, enemy_down.rect)  # 将爆炸的敌机画出来

    # 显示子弹
    player.bullets.draw(screen)
    # 显示敌机
    enemies1.draw(screen)

    # 绘制得分
    # pygame.font 用于加载和呈现字体的pygame模块
    # pygame.front.Font 从文件中创建一个新的字体对象:Font(filename, size) -> Font 或 Font(object, size) -> Font
    score_font = pygame.font.Font(None, 36)
    # pygame.front.Font.render:在新表面上绘制文本 render(text, antialias, color, background=None) ->Surface
    # Pygame 没有提供直接的方式在一个现有的 Surface 对象上绘制文本,使用 Font.render() 函数创建一个渲染了文本的图像（Surface 对象）
    # antilalias则是bool类型的值，用来控制文本的边是否是锯齿状的还是圆滑型的。后面分别是文本颜色和文本的背景颜色
    score_text = score_font.render('score: ' + str(score), True, (128, 128, 128))
    text_rect = score_text.get_rect()
    text_rect.topleft = [10, 10]
    screen.blit(score_text, text_rect)  # 将分数画出来

    # 更新屏幕
    pygame.display.update()

    # 处理游戏退出
    # pygame.event,get 从队列中获取事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # QUIT为pygame自带的事件
            pygame.quit()
            exit()

    # 获取键盘事件（上下左右按键）
    # pygame.key 模块: pygame模块与键盘一起工作
    key_pressed = pygame.key.get_pressed()  # 获取所有键盘按钮的状态
    # 返回一个布尔值序列，表示键盘上每个键的状态。使用键常量值来索引数组。True值表示按下了该按钮。

    # 处理键盘事件（移动飞机的位置）
    if key_pressed[K_w] or key_pressed[K_UP]:
        player.moveUp()
    if key_pressed[K_s] or key_pressed[K_DOWN]:
        player.moveDown()
    if key_pressed[K_a] or key_pressed[K_LEFT]:
        player.moveLeft()
    if key_pressed[K_d] or key_pressed[K_RIGHT]:
        player.moveRight()

# 游戏 Game Over 后显示最终得分
font = pygame.font.Font(None, 64)
text = font.render('Final Score: ' + str(score), True, (255, 0, 0))
text_rect = text.get_rect()
text_rect.centerx = screen.get_rect().centerx
text_rect.centery = screen.get_rect().centery + 24
screen.blit(game_over, (0, 0))
screen.blit(text, text_rect)

# 显示得分并处理游戏退出
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
