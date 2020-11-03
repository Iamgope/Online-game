import pygame

width = 500
length = 800

screen = pygame.display.set_mode((length, width))
pygame.display.set_caption("My_client")

clientNumber = 0


class player():
    def __init__(self, x, y, width, length, color):
        self.x = x
        self.y = y
        self.width = width
        self.length = length
        self.color = color
        self.recta = (x, y, width, length)
        self.vel = 3

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.recta)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.recta = (self.x, self.y, self.width, self.length)


def redraw(screen, player):
    screen.fill((0, 0, 0))
    player.draw(screen)
    pygame.display.update()


def main():
    flag = True
    p = player(50, 50, 100, 150, (0, 200, 0))
    clock = pygame.time.Clock()

    while flag:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
                pygame.quit()
        p.move()
        redraw(screen, p)


main()
