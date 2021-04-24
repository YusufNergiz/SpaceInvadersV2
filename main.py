import pygame
pygame.font.init()
# SCREEN #

WIDTH, HEIGHT = 750, 750
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders V2")
######################################################


# SPACESHIPS #

level_1_spaceship = pygame.image.load("level1spaceship.png")

######################################################

# ENEMY #

level_1_alien = pygame.image.load("level1alien.png")

######################################################

# LASER #

laser_1 = pygame.image.load("laser.png")


BG = pygame.transform.scale(pygame.image.load("background-black.png"), (WIDTH, HEIGHT))

class Ship:
    def __init__(self, x, y, health=100):
        self.x_position = x
        self.y_position = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        SCREEN.blit(self.ship_img, (self.x_position, self.y_position))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = level_1_spaceship
        self.laser_img = level_1_alien
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

class Enemy(Ship):
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img = level_1_alien
        self.laser_img = laser_1
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, velocity):
        self.y_position += velocity

def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    ship_velocity = 5

    player = Player(300, 650)
    clock = pygame.time.Clock()
    main_font = pygame.font.SysFont("comicsans", 50)

    def redraw_window():
        SCREEN.blit(BG, (0, 0))
        # draw text #
        lives_label = main_font.render(f"Lives: {lives}", True, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", True, (255, 255, 255))
        SCREEN.blit(level_label, (10, 10))
        SCREEN.blit(lives_label, (WIDTH - level_label.get_width() - 10, 10))
        player.draw(SCREEN)
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x_position - ship_velocity > 0: # LEFT
            player.x_position -= ship_velocity
        if keys[pygame.K_RIGHT] and player.x_position + ship_velocity < WIDTH - player.get_width(): # RIGHT
            player.x_position += ship_velocity
        if keys[pygame.K_UP] and player.y_position - ship_velocity > 0: # UP
            player.y_position -= ship_velocity
        if keys[pygame.K_DOWN] and player.y_position + ship_velocity < HEIGHT - player.get_height(): # DOWN
            player.y_position += ship_velocity



main()
