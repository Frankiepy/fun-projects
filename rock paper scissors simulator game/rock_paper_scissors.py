import pygame
import math
import random



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

    def __init__(self,type):
        super().__init__()
        self.type = type
        self.load_image = pygame.image.load(f'/Users/frankie/Downloads/FeedSDK-Python-master/good projects/{type}.png')
        # Load the player sprite

        self.image = pygame.Surface((50, 50))
        self.image.fill((100,100,100))

        # Set the initial position of the player
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,800)
        self.rect.y = random.randint(0,750)

        # Set the initial velocity of the player
        self.vel_x = random.randint(-2,2)
        self.vel_y = random.randint(-2,2)
    
    def change_type(self,type):
        self.type = type
        self.load_image = pygame.image.load(f'/Users/frankie/Downloads/FeedSDK-Python-master/good projects/{type}.png')
    
    def get_type(self):
        return self.type

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        # Keep the player sprite inside the screen boundaries
        if self.rect.x < 0:
            self.vel_x = abs(self.vel_x)  # Invert the x velocity to move right
            self.rect.x = 0

        elif self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.vel_x = -abs(self.vel_x)  # Invert the x velocity to move left
            self.rect.x = SCREEN_WIDTH - self.rect.width

        if self.rect.y < 0:
            self.vel_y = abs(self.vel_y)
            self.rect.y = 0  # Ensure the ball doesn't get stuck at the top

        elif self.rect.y > SCREEN_HEIGHT - self.rect.height:
            self.vel_y = -abs(self.vel_y)
            self.rect.y = SCREEN_HEIGHT - self.rect.height  # Ensure the ball doesn't go below the screen

        #print(self.vel_x)
        #print(self.vel_y)

# Create the player sprite
player = Player('rock')#rgb tuple

player2 = Player('paper')

player_list = []
player_positions = []

def generate_players(num_players=30):
    player_list = []
    options = ['rock','paper','scissors']
    for num in range(num_players):
        new_p = Player(random.choice(options))
        player_list.append(new_p)
        player_positions.append([new_p.rect.x, new_p.rect.y])
    return player_list

player_list = generate_players(30)

# Main game loop
running = True
while running:

    # Handle events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the player sprite
    # Clear the screen with the green background color
    screen.fill(BLACK)
    count = 0

    rock_set = {0,0}# have it store groups of positions
    paper_set = {0,0}
    scissors_set = {0,0}
    for player in player_list:
        player.update()
        screen.blit(player.load_image, player.rect)
        player_positions[count] = [player.rect.x, player.rect.y]
        count += 1

        x = player.rect.x
        xf = int(x/10)*10

        xf2, xf3 = xf-20, xf+20
        print(xf, xf2, xf3)

        y = player.rect.y
        yf = int(y/10)*10

        yf2, yf3 = yf-20, yf+20
        print(yf, yf2, yf3)

        if player.type == 'rock':
            rock_set.add(f"{xf}{yf}")
            rock_set.add(f"{xf}{yf2}")
            rock_set.add(f"{xf}{yf3}")
            rock_set.add(f"{xf2}{yf}")
            rock_set.add(f"{xf2}{yf2}")
            rock_set.add(f"{xf2}{yf3}")
            rock_set.add(f"{xf3}{yf}")
            rock_set.add(f"{xf3}{yf2}")
            rock_set.add(f"{xf3}{yf3}")
            p_set = paper_set.copy()
            p_len1 = len(paper_set)
            p_set.add(f"{xf}{yf}")
            p_set.add(f"{xf}{yf2}")
            p_set.add(f"{xf}{yf3}")
            p_set.add(f"{xf2}{yf}")
            p_set.add(f"{xf2}{yf2}")
            p_set.add(f"{xf2}{yf3}")
            p_set.add(f"{xf3}{yf}")
            p_set.add(f"{xf3}{yf2}")
            p_set.add(f"{xf3}{yf3}")
            if (p_len1+9) != len(p_set):
                #CONVERT ROCK TO PAPER
                player.change_type('paper')

        elif player.type == 'scissors':
            scissors_set.add(f"{xf}{yf}")
            scissors_set.add(f"{xf}{yf2}")
            scissors_set.add(f"{xf}{yf3}")
            scissors_set.add(f"{xf2}{yf}")
            scissors_set.add(f"{xf2}{yf2}")
            scissors_set.add(f"{xf2}{yf3}")
            scissors_set.add(f"{xf3}{yf}")
            scissors_set.add(f"{xf3}{yf2}")
            scissors_set.add(f"{xf3}{yf3}")

            r_set = rock_set.copy()
            r_len1 = len(rock_set)
            r_set.add(f"{xf}{yf}")
            r_set.add(f"{xf}{yf2}")
            r_set.add(f"{xf}{yf3}")
            r_set.add(f"{xf2}{yf}")
            r_set.add(f"{xf2}{yf2}")
            r_set.add(f"{xf2}{yf3}")
            r_set.add(f"{xf3}{yf}")
            r_set.add(f"{xf3}{yf2}")
            r_set.add(f"{xf3}{yf3}")
            if (r_len1+9) != len(r_set):
                #CONVERT ROCK TO PAPER
                player.change_type('rock')
        else:# == 'paper'
            paper_set.add(f"{xf}{yf}")
            paper_set.add(f"{xf}{yf2}")
            paper_set.add(f"{xf}{yf3}")
            paper_set.add(f"{xf2}{yf}")
            paper_set.add(f"{xf2}{yf2}")
            paper_set.add(f"{xf2}{yf3}")
            paper_set.add(f"{xf3}{yf}")
            paper_set.add(f"{xf3}{yf2}")
            paper_set.add(f"{xf3}{yf3}")
            s_set = scissors_set.copy()
            s_len1 = len(scissors_set)
            s_set.add(f"{xf}{yf}")
            s_set.add(f"{xf}{yf2}")
            s_set.add(f"{xf}{yf3}")
            s_set.add(f"{xf2}{yf}")
            s_set.add(f"{xf2}{yf2}")
            s_set.add(f"{xf2}{yf3}")
            s_set.add(f"{xf3}{yf}")
            s_set.add(f"{xf3}{yf2}")
            s_set.add(f"{xf3}{yf3}")
            if (s_len1+9) != len(s_set):
                #CONVERT ROCK TO PAPER
                player.change_type('scissors')


    # Draw the player sprite on the screen
    #screen.blit(player2.image, player2.rect)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    #clock.tick(60)

# Quit Pygame
pygame.quit()
