import sys, pygame

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
blue1 = pygame.Color("#197bd2")
blue2 = pygame.Color("#0f5cbf")
green = pygame.Color("#073127")

# General setup
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("direction_test")
clock = pygame.time.Clock()
FPS = 120

# Sprites
class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, color, radius):
        self.pos = pygame.math.Vector2(pos)
        self.image = pygame.Surface((radius*2, radius*2))
        self.image.set_colorkey(black)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=self.pos)

        self.mouse_pos = 0
        self.distance = 0
        self.dir = 0
        self.speed = 2

    def draw(self, win):
        win.blit(self.image, self.rect)

    def update(self):
        if self.distance:
            self.distance -= 1
            self.pos += self.dir * self.speed

            self.rect.center = (round(self.pos.x), round(self.pos.y))

    def set_mouse(self):
        self.mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos())
        self.mouse_pos = self.mouse_pos - self.pos
        self.distance = int(self.mouse_pos.magnitude()) // self.speed
        self.dir = self.mouse_pos.normalize()
        #print(f"dir: {self.dir}\nmouse_pos: {self.mouse_pos}")
       

ball_0 = Ball((WIDTH//2, HEIGHT//2), blue1, 20)

# Game loop
def main():
    pygame.init()
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    ball_0.set_mouse()

        # Draw / update sprite
        WIN.fill(black)
        ball_0.draw(WIN)
        ball_0.update()

        # Update display
        pygame.display.flip()
        clock.tick(FPS)


    pygame.quit()
    sys.exit(0)

if __name__ == '__main__':
    main()
