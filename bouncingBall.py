import pygame
import math
import random
import simpleaudio as sa


class Ball:
    def __init__(self, position, speed, color):
        self.position = position
        self.speed = speed
        self.direction = pygame.Vector2(1, 0).rotate(random.randint(0, 360))
        self.color = color
    
    def update(self, dt):
        self.position += self.direction * dt * self.speed

    def is_hitting_border(self):
        distance = math.sqrt(abs((self.position.y - 400) ** 2) + abs((self.position.x - 400) ** 2))
        return distance >= 340

pygame.init()
pygame.mixer.init()
boop_sound = pygame.mixer.Sound("COUNT5.wav")
ria_sound = pygame.mixer.Sound('/Users/jake.langlois/Documents/ria.wav')
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True
dt = 0
center = pygame.Vector2(400, 400)
player_pos = pygame.Vector2(400, 400)
ball_speed = 35
gravity = pygame.Vector2(0, 3.5)
ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

initial_position = pygame.Vector2(random.randint(200, 600), random.randint(200, 600))

balls = [Ball(initial_position, ball_speed, ball_color)]
    

while running:
    #User clicks X to close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("black")

    # Draws all the balls on the screen
    for ball in balls:
        pygame.draw.circle(screen, ball.color, (int(ball.position.x), int(ball.position.y)), 10)

    ## Draws the circular border
    pygame.draw.circle(screen, "white", [400, 400], 350, 3)

    # Gravitys affect on the balls
    for ball in balls:
        ball.direction += gravity * dt

    ballCount = 0
    
    # Constantly updates the position of the ball
    for ball in balls:
        ball.update(dt)

        if ball.is_hitting_border():
            boop_sound.play()
            ria_sound.play()

            direction_to_center = (ball.position - center)
            ball.direction = ball.direction.reflect(direction_to_center)

            new_ball = Ball(pygame.Vector2(random.randint(200, 600), random.randint(100, 600)), 
                            ball_speed,(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            balls.append(new_ball)

    #Renders Game
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()