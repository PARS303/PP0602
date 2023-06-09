import pygame
import random

def drawSquare(screen, position, color, caption=""):
    """
        Draw on the screen on position x, y (x and y are not coordinates, they're the grid position!)
        Upperleft square is 0,0
    """
    screen.fill(color, (position[0] * w + 1, position[1] * h + 1, w - 1, h - 1))
    pygame.display.set_caption(caption)

    pygame.display.set_caption("Жоский отдых 'Змейка' ")


class Food:
    def __init__(self, screen, x, y, color, nutrition):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color
        self.nutrition = nutrition

    def givePos(self):
        return (self.x, self.y)

    def draw(self):
        drawSquare(self.screen, self.givePos(), self.color)

class Snake:
    def __init__(self, screen, bgcolor, x, y, color, grow_to=2):
        self.screen = screen
        self.bgcolor = bgcolor
        self.x = x
        self.y = y
        self.color = color
        self.grow_to = grow_to - 1

        self.vx = 0
        self.vy = 0
        self.body = []
        self.crashed = False
        self.length = 0

        self.speed = 1

    def eat(self, n):
        self.grow_to += n

    def givePos(self):
        return (self.x, self.y)

    def keyHandler(self, event):
        try:
            if (event.key == pygame.K_UP and (self.x, self.y - 1) != self.body[0]):
                self.vx = 0
                self.vy = -self.speed
            elif (event.key == pygame.K_DOWN and (self.x, self.y + 1) != self.body[0]):
                self.vx = 0
                self.vy = self.speed
            elif (event.key == pygame.K_LEFT and (self.x - 1, self.y) != self.body[0]):
                self.vx = -self.speed
                self.vy = 0
            elif (event.key == pygame.K_RIGHT and (self.x + 1, self.y) != self.body[0]):
                self.vx = self.speed
                self.vy = 0
        except:
            if (event.key == pygame.K_UP):
                self.vx = 0
                self.vy = -self.speed
            elif (event.key == pygame.K_DOWN):
                self.vx = 0
                self.vy = self.speed
            elif (event.key == pygame.K_LEFT):
                self.vx = -self.speed
                self.vy = 0
            elif (event.key == pygame.K_RIGHT):
                self.vx = self.speed
                self.vy = 0

    def draw(self):
        drawSquare(self.screen, (self.x, self.y), self.color)

    def move(self):
        if (self.vx != 0 or self.vy != 0):
            self.body.insert(0, (self.x, self.y))

        self.x += self.vx
        self.y += self.vy

        if ((self.x, self.y) in self.body):
            self.crashed = True
            return False

        if (self.x < 0 or self.x >= wid):
            self.crashed = True
            return False
        if (self.y < 0 or self.y >= hei):
            self.crashed = True
            return False

        drawSquare(self.screen, (self.x, self.y), self.color)

        if (self.grow_to > self.length):
            self.length += 1


        if (len(self.body) > self.length):
            drawSquare(self.screen, self.body.pop(), self.bgcolor)

x = 1  # Размер поля 15x15
y = 1  # Скорость Slow

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

bgcolor = white

fruitcolors = [black, white, red, green, blue]

width = 600
height = 600

if (x == 1):
    wid = 15
    hei = 15

w = width // wid
h = height // hei

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

if (y == 1):
    speed = 5

running = True

screen.fill(bgcolor)
for i in range(w, width, w):
    pygame.draw.line(screen, black, (i, 0), (i, height))
for i in range(h, height, h):
    pygame.draw.line(screen, black, (0, i), (height, i))

snake = Snake(screen, bgcolor, wid // 2 - 1, hei // 2 - 1, black, 5)
snake.draw()

if (snake.color in fruitcolors):
    fruitcolors.remove(snake.color)

if (bgcolor in fruitcolors):
    fruitcolors.remove(bgcolor)

foo = random.randint(0, wid - 1)
bar = random.randint(0, hei - 1)
while ((foo, bar) in snake.body):
    foo = random.randint(0, wid - 1)
    bar = random.randint(0, hei - 1)

food = Food(screen, foo, bar, fruitcolors[random.randint(0, len(fruitcolors) - 1)], 1)
food.draw()

pygame.display.flip()

while running:

    snake.move()

    if (snake.crashed):
        running = False
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        if (event.type == pygame.KEYDOWN):
            snake.keyHandler(event)

    if (snake.givePos() == food.givePos()):
        snake.eat(food.nutrition)
        foo = random.randint(0, wid - 1)
        bar = random.randint(0, hei - 1)
        while ((foo, bar) in snake.body):
            foo = random.randint(0, wid - 1)
            bar = random.randint(0, hei - 1)
        food = Food(screen, foo, bar, fruitcolors[random.randint(0, len(fruitcolors) - 1)], 1)
        food.draw()

    pygame.display.flip()
    clock.tick(speed)
