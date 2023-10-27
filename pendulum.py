import math
import matplotlib.pyplot as plt
import pygame
import time

# Import the required libraries

def form_line(startingx, startingy, length, angle):
    if angle < 90 or angle > 90:
        #ratio = math.sin(math.radians(90)/length
        #ratio2 = math.sin(math.radians(angle)/x
        print((math.sin(math.radians(30))*170)/math.sin(math.radians(90)))
        x_length = (math.sin(math.radians(angle)) * length)/math.sin(math.radians(90))#for horizontal distance
        x2_length = (math.sin(math.radians(90-angle)) * length)/math.sin(math.radians(90))# for vertical distance
        print(x_length)
        print(x2_length)
        posx = startingx - x_length
        posy = startingy + x2_length
        return [posx, posy]
    elif angle == 90:
        return [startingx - length,startingy]
    else: # negatives are working very well, >90 has issues
        angle2 = angle-90
        x_length = (math.sin(math.radians(angle2)) * length)/math.sin(math.radians(90))#for horizontal distance
        x2_length = (math.sin(math.radians(90-angle2)) * length)/math.sin(math.radians(90))# for vertical distance
        print(x_length)
        print(x2_length)
        posx = startingx - x_length
        posy = startingy - x2_length
        return [posx, posy]

pygame.init()
width = 800
height = 600
window = pygame.display.set_mode((width, height))
line_color = (255, 0, 0)  # Red color (RGB format)

#θ''(t) + (b/m)θ'(t) + (g/L)sin(θ(t)) = 0

l = 1 #Length of the  (L): 1
m = 0.5 #Mass of the  bob (m): 0.5 kg
b = 0.1 #Damping coefficient due to air resistance (b): 0.1 kg/s
g = 9.8 #Acceleration due to gravity (g): 9.8 m/s^2

t = 0 #(initial time)
θ = 179 * (math.pi/180) #(initial angular displacement) measured in radians (pi circle) # can't be greater than 180 or pi
θ1=0 #θ' = 0 (initial angular velocity)
time_step = 0.1 #how much time moves

times = [0]
angular_displacements = [0]

while t < 100:
    time.sleep(.05)
    θ2 = -((b/m)*θ1) - ((g/l)*math.sin(θ))

    θ1 = θ1 + θ2 * time_step
    θ = θ + θ1 * time_step
    t = t + time_step
    times.append(t)
    angular_displacements.append(θ)
    
    angle = θ*180/math.pi
    x,y = form_line(250,200,150,angle)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))  # Fill the window with black color
    #pygame.draw.line(window, line_color, (250,100),(250,290), 3)  # Draw the line
    pygame.draw.line(window, line_color, (250, 200), (x, y), 3)  # Draw the line
    pygame.display.flip()

pygame.quit()
    

#Plot the angular displacement (θ) as a function of time (t) using a graphing tool or programming language.

plt.plot(times, angular_displacements)
plt.ylabel('angular displacement')
plt.xlabel('time')
plt.show()