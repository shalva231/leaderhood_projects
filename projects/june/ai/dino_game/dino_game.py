import pygame
import os
import random

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FONT = pygame.font.Font('freesansbold.ttf', 20)

script_dir = os.path.dirname(os.path.abspath(__file__))

assets_dir = os.path.join(script_dir, "Assets")
dino_dir = os.path.join(assets_dir, "Dino")
bird_dir = os.path.join(assets_dir, "Bird")
cactus_dir = os.path.join(assets_dir, "Cactus")
other_dir = os.path.join(assets_dir, "Other")

dino_run1_path = os.path.join(dino_dir, "DinoRun1.png")
dino_run2_path = os.path.join(dino_dir, "DinoRun2.png")
dino_jump_path = os.path.join(dino_dir, "DinoJump.png")
dino_duck1_path = os.path.join(dino_dir, "DinoDuck1.png")
dino_duck2_path = os.path.join(dino_dir, "DinoDuck2.png")
dino_dead_path = os.path.join(dino_dir, "DinoDead.png")
dino_start_path = os.path.join(dino_dir, "DinoStart.png")

bird1_path = os.path.join(bird_dir, "Bird1.png")
bird2_path = os.path.join(bird_dir, "Bird2.png")

large_cactus1_path = os.path.join(cactus_dir, "LargeCactus1.png")
large_cactus2_path = os.path.join(cactus_dir, "LargeCactus2.png")
large_cactus3_path = os.path.join(cactus_dir, "LargeCactus3.png")
small_cactus1_path = os.path.join(cactus_dir, "SmallCactus1.png")
small_cactus2_path = os.path.join(cactus_dir, "SmallCactus2.png")
small_cactus3_path = os.path.join(cactus_dir, "SmallCactus3.png")

cloud_path = os.path.join(other_dir, "Cloud.png")
bg_path = os.path.join(other_dir, "Track.png")

RUNNING = [pygame.image.load(dino_run1_path),
           pygame.image.load(dino_run2_path)]
JUMPING = pygame.image.load(dino_jump_path)
DUCKING = [pygame.image.load(dino_duck1_path),
           pygame.image.load(dino_duck2_path)]
DEAD = pygame.image.load(dino_dead_path)
START = pygame.image.load(dino_start_path)

BIRD = [pygame.image.load(bird1_path),
        pygame.image.load(bird2_path)]

LARGE_CACTUS = [pygame.image.load(large_cactus1_path),
                pygame.image.load(large_cactus2_path),
                pygame.image.load(large_cactus3_path)]
SMALL_CACTUS = [pygame.image.load(small_cactus1_path),
                pygame.image.load(small_cactus2_path),
                pygame.image.load(small_cactus3_path)]

CLOUD = pygame.image.load(cloud_path)
BG = pygame.image.load(bg_path)

class Dino:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False
        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)

class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325

class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index//5], self.rect)
        self.index += 1

def background():
    global x_pos_bg, y_pos_bg
    image_width = BG.get_width()
    SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
    SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
    if x_pos_bg <= -image_width:
        x_pos_bg = 0
    x_pos_bg -= game_speed

def main():
    global game_speed, points, obstacles, x_pos_bg, y_pos_bg
    run = True
    clock = pygame.time.Clock()
    cloud = Cloud()
    player = Dino()
    obstacles = []
    death_count = 0
    points = 0
    game_speed = 10  # Start with initial game speed
    x_pos_bg = 0  # Initialize x_pos_bg
    y_pos_bg = 380  # Initialize y_pos_bg

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1  # Increase speed every 100 points
        text = FONT.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)

        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(30)
        pygame.display.update()

def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                main()

menu(death_count=0)
