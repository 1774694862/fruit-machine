import random, time
import sys, pygame

map = []

# rows = 35
# clos = 35
rows = 7
clos = rows

cell_size = 80  # 一个网格的大小
sourceHeight = 0
buttunHeight = 200
funWidth = 200
mapWidth = clos * cell_size
mapHeight = rows * cell_size

screen = pygame.display.set_mode((mapWidth + buttunHeight, mapHeight + funWidth))
pygame.display.set_caption("tiger")
clock = pygame.time.Clock()

pygame.font.init()
pygame.init()

# 背景图片
apple_img = pygame.image.load('images/apple.jpg')
watermelon_img = pygame.image.load('images/watermelon.jpg')
orange_img = pygame.image.load('images/orange.jpg')
bell_img = pygame.image.load('images/bell.jpg')
mango_img = pygame.image.load('images/mango.jpg')
star_img = pygame.image.load('images/star.jpg')
banana_img = pygame.image.load('images/banana.jpg')
good_img = pygame.image.load('images/good.jpg')

BLACK = (0, 0, 0)
RED = (244, 64, 76)
GREEN = (45, 162, 72)
BLUE = (65, 69, 255)
ORANGE = (255, 127, 0)
CYAN = (0, 183, 235)
MAGENTA = (239, 45, 171)
YELLOW = (245, 200, 22)
WHITE = (255, 255, 255)

RED_2 = (215, 0, 15)  # 中国红
GREEN_2 = (121, 139, 113)  # 莫兰蒂
GREEN_3 = (1, 132, 127)  # 马尔斯绿
BLUE_2 = (0, 46, 166)  # 克兰因蓝
BLUE_3 = (1, 62, 119)  # 普鲁士蓝
YELLOW_2 = (252, 218, 94)  # 拿坡里黄
ORANGE_2 = (255, 119, 15)  # 爱马仕橙

bg1 = (222, 222, 222)
bg = (WHITE)
line_width = 4
score = 100
get_score = 0

main_button_color = (255, 200, 102)

apple = 0
orange = 0
bell = 0
watermelon = 0
mango = 0
star = 0
banana = 0
lucky = 0

colorss = [BLACK, RED, GREEN, BLUE, ORANGE, CYAN, MAGENTA, YELLOW, WHITE]
colors = [BLACK, RED_2, GREEN_2, GREEN_3, BLUE_2, BLUE_3, ORANGE_2]

fps = 1

step_list = [51, 25, 15, 7, 3, 2, 1, 1, 1, 0]  # 每一个速度需要走多少格子  跑马灯
pfs_list = [2, 5, 10, 15, 20, 25, 30, 40, 50, 999]  # 跑马灯每个阶段的速度
# step_list = [24, 0]  # 每一个速度需要走多少格子  跑马灯
# pfs_list = [2, 999]  # 跑马灯每个阶段的速度

class Game:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, cell_size, cell_size)  # 当前语言绘制的正方形
        self.x, self.y = 0, 0
        self.color_key = random.randint(0, len(colors) - 1)
        self.key = 0
        self.speed = pfs_list[self.key]
        self.fps = pfs_list[self.key]
        self.go = False
        self.step_num = 0
        self.G = False
        self.rect_position = 0  # 当前方块位置 初始为0 (0-23)

    # 绘制移动的方块
    def draw(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        random_color = pygame.color.Color((r, g, b))
        if not self.go:
            random_color = colors[self.color_key]
        if self.fps == fps:
            random_color = pygame.color.Color((r, g, b))
        self.rect.topleft = self.x * cell_size + line_width - 1, self.y * cell_size + line_width - 1

        pygame.draw.rect(screen, random_color, (self.rect.x, self.rect.y, cell_size - 5, cell_size - 5),
                         0)

    def move(self):

        if self.y == 0 and rows - 1 > self.x >= 0:
            self.x += 1
        elif self.x == rows - 1 and rows - 1 > self.y >= 0:
            self.y += 1
        elif self.y == rows - 1 and rows > self.x > 0:
            self.x -= 1

        elif self.x == 0 and rows > self.y > 0:
            self.y -= 1

    def add_score(self):
        global get_score
        global score
        s = [(3, 3), (3, 83), (3, 163), (3, 243), (3, 323), (3, 403), (3, 483),  # 第一列
             (83, 3), (163, 3), (243, 3), (323, 3), (403, 3), (483, 3),  # 第一行
             (83, 483), (163, 483), (243, 483), (323, 483), (403, 483),  # 第二行
             (483, 83), (483, 163), (483, 243), (483, 323), (483, 403), (483, 483)]
        fruit = [apple, star, orange, lucky, banana, watermelon, apple,
                 star, banana, lucky, orange, mango, apple,
                 watermelon, orange, lucky, banana, bell,
                 mango, banana, lucky, orange, bell, apple
                 ]
        add = [1, 2, 1, 100, 1, 2, 1,
               2, 1, 100, 1, 2, 1,
               2, 1, 100, 1, 2,
               2, 1, 100, 1, 2, 1
               ]
        for i in range(len(s)):
            if s[i] == self.rect.topleft:
                get_score += fruit[i] * add[i] * 2
        score += get_score

    def img_display(self):

        img_list = [apple_img, banana_img, watermelon_img, orange_img, bell_img, mango_img, star_img, good_img]

        img_list_1 = [apple_img, star_img, banana_img, good_img, orange_img, mango_img, apple_img]
        img_list_2 = [apple_img, mango_img, banana_img, good_img, orange_img, bell_img, apple_img]
        img_list_3 = [apple_img, watermelon_img, orange_img, good_img, banana_img, bell_img, apple_img]
        img_list_4 = [apple_img, star_img, orange_img, good_img, banana_img, watermelon_img, apple_img]

        for i in range(len(img_list_1)):
            screen.blit(img_list_1[i], (10 + cell_size * i, 10))

            # print("ss")
        for i in range(len(img_list_2)):
            screen.blit(img_list_2[i], (10 + cell_size * (clos - 1), 10 + cell_size * i))
        for i in range(len(img_list_3)):
            screen.blit(img_list_3[i], (10 + cell_size * i, 10 + cell_size * (clos - 1)))
        for i in range(len(img_list_4)):
            screen.blit(img_list_4[i], (10, 10 + cell_size * i))

    # 按钮积分清零
    def zero(self):
        global apple, orange, bell, watermelon, mango, star, banana, lucky
        apple, orange, bell, watermelon, mango, star, banana, lucky = 0, 0, 0, 0, 0, 0, 0, 0

    def run(self):

        if self.fps >= 100:
            self.go = False
            self.add_score()
            print("你本次得到的分数：",get_score)
            self.zero()
            # 按钮积分清零
            self.rect_position = (self.rect_position + sum(step_list)-step_list[-1]) % 24   #最后一个位置step_list[-1]不会走
            self.G = False
            return

        self.speed -= 1  # 40s 之内减少到0
        if self.speed == 0:  # 每间隔 fps 时间就会走一格子，fps=60 表示一秒
            self.speed = self.fps

            # self.speed = levels[self.level]
            self.step_num += 1
            self.move()
        # print(time.time())
        if self.step_num == step_list[self.key]:
            self.key += 1
            self.fps = pfs_list[self.key]

            self.step_num = 0

    def display(self):
        self.draw()
        self.draw_grid(bg, line_width, cell_size, GREEN_3)
        self.img_display()
        if self.go:
            self.run()

    def start_game(self):
        if not self.go:
            global get_score
            get_score = 0
            step_list[0] = random.randint(31, 55)
            if self.G:
                self.mystical_power()
            # print(self.G)
            self.key = 0
            self.fps = pfs_list[self.key]
            self.speed = pfs_list[self.key]
            self.go = True

    def mystical_power(self):
        # print("*********************start*********************")
        fruit_dict = {'apple': [0, 6, 12, 18], 'star': [1, 23], 'orange': [4, 10, 16, 22], 'lucky': [3, 9, 15, 21],
                      'banana': [2, 8, 14, 20], 'watermelon': [17, 19], 'mango': [5, 7], 'bell': [11, 13]}
        global apple, orange, bell, watermelon, mango, star, banana, lucky
        max_sc = max(max(max(apple, orange), max(bell, watermelon)), max(max(mango, star), banana))
        now_position = 0
        if max_sc == apple:
            now_position = random.choice(fruit_dict['apple'])
        if max_sc == star:
            now_position = random.choice(fruit_dict['star'])
        if max_sc == orange:
            now_position = random.choice(fruit_dict['orange'])
        if max_sc == lucky:
            now_position = random.choice(fruit_dict['lucky'])
        if max_sc == banana:
            now_position = random.choice(fruit_dict['banana'])
        if max_sc == watermelon:
            now_position = random.choice(fruit_dict['watermelon'])
        if max_sc == mango:
            now_position = random.choice(fruit_dict['mango'])
        if max_sc == bell:
            now_position = random.choice(fruit_dict['bell'])
        mystical_power_data = 0
        for i in range(24):
            finaly_step = (sum(step_list)-step_list[0]+i+self.rect_position)%24
            if finaly_step == now_position:
                mystical_power_data = i
                break

        step_list[0] = random.choice([24,48])+mystical_power_data
        # print("下注的水果所在的位置", now_position)
        # print("下注分数", max_sc)
        # print("方块当前位置",self.rect_position)
        # print("方块最少需要走多少步才会中奖", mystical_power_data)
        # print("方块本次会走多少步",sum(step_list))
        # print("最终的位置", (sum(step_list) + self.rect_position) % 24)
        # print("*********************start*********************")
    def draw_grid(self, background, line_width, cell_size, line_color):
        # return
        for i in range(rows + 1):
            pygame.draw.line(screen, line_color, (0, sourceHeight + i * cell_size),
                             (mapWidth, sourceHeight + i * cell_size), line_width)
            if 1 < i < 6:
                pygame.draw.line(screen, background, (cell_size, sourceHeight + i * cell_size),
                                 (mapWidth - cell_size, sourceHeight + i * cell_size),
                                 line_width)

            # 画a玩家行线
        # pygame.draw.line()  # 画b玩家行线
        for i in range(clos + 1):
            pygame.draw.line(screen, line_color, (i * cell_size, sourceHeight + 0),
                             (i * cell_size, sourceHeight + mapHeight), line_width)
            if 1 < i < 6:
                pygame.draw.line(screen, background, (i * cell_size, sourceHeight + cell_size),
                                 (i * cell_size, sourceHeight + mapHeight - cell_size), line_width)
            # 画a玩家列线
        # pygame.draw.line()  # 画b玩家列线


class Text:
    def __init__(self):
        self.now_time = 0
        self.last_time = 0
        self.step = 0
        self.font = pygame.font.SysFont('Sim Hei', 25)  # 设置字体
        self.source_color = BLUE_3
        self.xiazhu = False

    def fps(self):
        self.now_time = time.time()
        fps = int(1 / (self.now_time - self.last_time))
        # print(fps)
        self.last_time = self.now_time
        text = self.font.render("fps:" + str(int(fps)), True, self.source_color)
        screen.blit(text, (mapWidth + funWidth - 85, 10))

    def test_time(self):
        text = self.font.render(str(round(pygame.time.get_ticks() / 1000, 2)), True, self.source_color)
        screen.blit(text, (mapWidth + funWidth - 175, 10))

    def my_test(self, text, color, xx, yy):
        your_text = self.font.render(str(text), True, color)
        screen.blit(your_text, (xx, yy))

    def source_now(self):
        score_text = self.font.render(str(score), True, self.source_color)
        self.my_test("NOW", self.source_color, mapWidth / 2 + 50, mapWidth / 2 - 40)
        screen.blit(score_text, (mapWidth / 2 + 50, mapWidth / 2))

    def source_get(self):
        score_text = self.font.render(str(get_score), True, self.source_color)
        self.my_test("GET", self.source_color, mapWidth / 2 - 80, mapWidth / 2 - 40)
        screen.blit(score_text, (mapWidth / 2 - 80, mapWidth / 2))

    def help_xia(self):
        self.my_test("下注！！！", self.source_color, mapWidth + 50, 350)

    def display(self):
        self.source_now()
        self.source_get()
        self.fps()
        # self.test_time()
        if self.xiazhu:
            self.help_xia()


class Button:

    # 初始化 显示文本，坐标，背景颜色，字体背景颜色，字体大小
    def __init__(self, text, x1, y1, button_width=88, button_height=55, bg_color=(1, 222, 222), text_color=BLACK,
                 text_size=20, ):
        self.x1 = x1
        self.y1 = y1
        self.text = text
        self.bg_color = bg_color
        self.old_color = bg_color
        self.text_color = text_color
        self.text_size = text_size
        self.help = []
        self.bg_image = 0  # dangqian de背景图片
        self.button_width = button_width  # 按钮 宽度
        self.button_height = button_height  # 按钮高度
        # self.size = size

    # 显示按钮
    def draw(self, source=-1):
        pygame.draw.rect(screen, self.bg_color, (self.x1, self.y1, self.button_width, self.button_height))

        # 画文字Arial Black
        font = pygame.font.SysFont('Sim Hei', self.text_size)  # 设置字体
        text = font.render(self.text, True, self.text_color)
        t_w, t_h = text.get_size()
        screen.blit(text, (self.x1 + self.button_width / 2 - t_w / 2, self.y1 + self.button_height / 2 - t_h / 2))

        if source != -1:
            sourc = font.render(str(source), True, self.text_color)
            screen.blit(sourc, (
                self.x1 + self.button_width / 2 - t_w / 2 + 0, self.y1 + self.button_height / 2 - t_h / 2 - 50))

    # 如果按钮摁下
    def is_down(self, pos):
        m_x, m_y = pos
        if self.x1 < m_x < self.x1 + self.button_width and self.y1 < m_y < self.y1 + self.button_height:
            self.bg_color = main_button_color
            self.draw()
            return True
        else:
            self.bg_color = self.old_color
            self.draw()

            return False

    def get_button_width(self):
        return self.button_width

    def is_up(self, pos):
        m_x, m_y = pos
        if not (self.x1 < m_x < self.x1 + self.button_width and self.y1 < m_y < self.y1 + self.button_height):
            self.bg_color = self.old_color
            self.draw()
            return True
        return False


text = Text()
game = Game()

start_dis = 20
add_button = 100
apple_button = Button("苹果", start_dis, mapHeight + 100)
orange_button = Button("橘子", start_dis + add_button * 1, mapHeight + 100)
bell_button = Button("铃铛", start_dis + add_button * 5, mapHeight + 100)
watermelon_button = Button("西瓜", start_dis + add_button * 3, mapHeight + 100)
mango_button = Button("芒果", start_dis + add_button * 4, mapHeight + 100)
star_button = Button("星星", start_dis + add_button * 6, mapHeight + 100)
banana_button = Button("香蕉", start_dis + add_button * 2, mapHeight + 100)

start_button = Button("开始游戏", mapWidth + 60, 400)
add_button = Button("投币", mapWidth + 60, 100)
# source_button_get = Button()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #     键盘
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:  # waigua
                game.G = True
        # 2.鼠标按下对应的事件（确定反应范围）
        if event.type == pygame.MOUSEBUTTONDOWN:
            if add_button.is_down(event.pos):
                score += 10
            if start_button.is_down(event.pos):
                if apple + orange + bell + watermelon + mango + star + banana <= 0:
                    text.xiazhu = True
                else:
                    text.xiazhu = False
                    game.start_game()
            if score > 0 and not game.go:
                if apple_button.is_down(event.pos):
                    apple += 10
                    score -= 10
                if orange_button.is_down(event.pos):
                    orange += 10
                    score -= 10
                if bell_button.is_down(event.pos):
                    bell += 10
                    score -= 10
                if watermelon_button.is_down(event.pos):
                    watermelon += 10
                    score -= 10
                if mango_button.is_down(event.pos):
                    mango += 10
                    score -= 10
                if star_button.is_down(event.pos):
                    star += 10
                    score -= 10
                if banana_button.is_down(event.pos):
                    banana += 10
                    score -= 10

    # 背景颜色
    screen.fill(bg)

    # display
    game.display()
    text.display()

    # 按钮显示
    apple_button.draw(apple)
    orange_button.draw(orange)
    bell_button.draw(bell)
    watermelon_button.draw(watermelon)
    mango_button.draw(mango)
    star_button.draw(star)
    banana_button.draw(banana)
    add_button.draw(10)
    # 按钮的悬浮变色
    mouse = pygame.mouse.get_pos()
    if apple_button.is_down(mouse):
        pass
    if orange_button.is_down(mouse):
        pass
    if bell_button.is_down(mouse):
        pass
    if watermelon_button.is_down(mouse):
        pass
    if mango_button.is_down(mouse):
        pass
    if star_button.is_down(mouse):
        pass
    if banana_button.is_down(mouse):
        pass
    if add_button.is_down(mouse):
        pass
    if start_button.is_down(mouse):
        pass
    pygame.display.update()
    clock.tick(60)
