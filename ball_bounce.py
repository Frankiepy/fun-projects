import pygame
import math



# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Set the dimensions of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 750

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the caption of the window
pygame.display.set_caption("Movable Sprite")

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Define a class for the player sprite
class Player(pygame.sprite.Sprite):

    def __init__(self,color,pos=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 8)):
        super().__init__()
        self.color = color
        # Load the player sprite
        self.image = pygame.Surface((30, 30))
        self.image.fill(self.color)

        # Set the initial position of the player
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        # Set the initial velocity of the player
        self.vel_x = 2
        self.vel_y = 0

    def update(self):
        # Move the player sprite
        # 9.8 m/s^2
        self.vel_y += 9.8/60
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        self.vel_x, self.vel_y = change([self.rect.x,self.rect.y],self.vel_x,self.vel_y)
        # Keep the player sprite inside the screen boundaries
        #if self.rect.x < 0:
        #    self.vel_x = abs(self.vel_x)  # Invert the x velocity to move right
        #    self.rect.x = 0

        #elif self.rect.x > SCREEN_WIDTH - self.rect.width:
        #    self.vel_x = -abs(self.vel_x)  # Invert the x velocity to move left
        #    self.rect.x = SCREEN_WIDTH - self.rect.width

        #if self.rect.y < 0:
        #    self.vel_y = abs(self.vel_y)/1.5
        #    self.rect.y = 0  # Ensure the ball doesn't get stuck at the top

        #elif self.rect.y > SCREEN_HEIGHT - self.rect.height:
        #    self.vel_y = -abs(self.vel_y)/1.5
        #    self.rect.y = SCREEN_HEIGHT - self.rect.height  # Ensure the ball doesn't go below the screen

        #print(self.vel_x)
        #print(self.vel_y)

# Create the player sprite
player = Player((255,255,255),(SCREEN_WIDTH/2,SCREEN_HEIGHT/8+20))#rgb tuple

#player2 = Player((243,134,214))

def change(pos,vel_x,vel_y):
    x = int(pos[0])
    y = int(pos[1])
    x_vel_change = .5
    y_vel_change = 0
    halfway_point = 400
    325,15
    y1 = int(SCREEN_HEIGHT/2 + math.sqrt(375**2-(x-SCREEN_WIDTH/2)**2))
    y2 = int(SCREEN_HEIGHT/2 - math.sqrt(375**2-(x-SCREEN_WIDTH/2)**2))
    print(y,y1,y2)
    if y > y1:
        #print(0/0)
        (x - 25)*.5/400
        x_vel_change -= (x - 25)*.5/400
        y_vel_change += (x - 25)*.5/400
        if y_vel_change > .5:
            y_vel_change = .5 - y_vel_change

        vel_y = -abs(vel_y)/(1+y_vel_change)
        vel_x = -abs(vel_x)/(1+x_vel_change)
    elif y < y2:
        #OPP VELOCHANGE
        (x - 25)*.5/400
        x_vel_change -= (x - 25)*.5/400
        y_vel_change += (x - 25)*.5/400
        if y_vel_change > .5:
            y_vel_change = .5 - y_vel_change

        vel_y = abs(vel_y)/(1+y_vel_change)
        vel_x = abs(vel_x)/(1+x_vel_change)

    return vel_x, vel_y

# Main game loop
running = True
while running:

    # Handle events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the player sprite
    #player2.update()
    player.update()
    # Clear the screen with the green background color
    screen.fill(BLACK)
    for x in range(25,775):
        y = SCREEN_HEIGHT/2 + math.sqrt(375**2-(x-SCREEN_WIDTH/2)**2)
        y2 = SCREEN_HEIGHT/2 - math.sqrt(375**2-(x-SCREEN_WIDTH/2)**2)
        pygame.draw.circle(screen, (243,134,214), (x, y), 1)
        pygame.draw.circle(screen, (243,134,214), (x, y2), 1)

    # Draw the player sprite on the screen
    screen.blit(player.image, player.rect)
    #screen.blit(player2.image, player2.rect)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
