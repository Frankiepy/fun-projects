# Simple Snake Game in Python 3 for Beginners
# By @TokyoEdTech

import turtle
import time
import random
import numpy

#delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @TokyoEdTech")
wn.bgcolor("green")
wn.setup(width=1200, height=780)
wn.tracer(0) # Turns off the screen updates

# Snake snakes[i]/ make snakes
snakes = {}
class Snake:
    def __init__(self, num):
        self.num = num
    
    def brain(self, food_pos):#, segments_pos, head_pos):
        for i in snakes:
            #pos = [snakes[i].xcor(), snakes[i].ycor()]
            food_x_dif = snakes[i].xcor() + food_pos[0]
            food_y_dif = snakes[i].ycor() + food_pos[1]
            print(f"food: {food_x_dif},{food_y_dif}")
            #segs_x_difs = [segment[0] for segment in segments_pos]
            #segs_y_difs = [segment[1] for segment in segments_pos]
            
            #left_wall = snakes[i].xcor() - 260
            #right_wall = snakes[i].ycor() - 260


            w1 = snakes[i].dna[0] #numpy.random.uniform(-1.0, 1.0, 1)
            w2 = snakes[i].dna[1] #numpy.random.uniform(-1.0, 1.0, 1)
            
            print(w1, w2)

            choice_num = (food_x_dif*w1 + food_y_dif*w2)/2 # draw it out so if left or down value is negative

            # highest possible = f1 + f2, lowest = -f1-f2 , middle = 0
            print(f"choice: {choice_num}")
            if choice_num > (food_x_dif + food_y_dif)*.75: #20 + 20 = 40*.75 = 30
                go_up(i)
            elif choice_num > (food_x_dif + food_y_dif)*.5:
                go_down(i)
            elif choice_num > (food_x_dif + food_y_dif)*.25:
                go_left(i)
            else:
                go_right(i)
                
            #snakes[i].dna
            #snakes[i].decision = pos
        #self.food_pos = food_pos
        #self.segments_pos = segments_pos
        #self.head_pos = head_pos
        

    def create(self, scores):
        for x in range(0,self.num):
            p2 = 0
            p1 = 0
            if len(scores) > 5:
                    total_scores = 0
                    for i in scores:
                        total_scores += i[0]
    
                    probability_spot = 0
                    pick1 = random.randint(0,total_scores)
                    pick2 = random.randint(0,total_scores)

                    for i in scores:
                        if pick1 in range(probability_spot, probability_spot+i[0]+1): # BAD DOESNT WORK
                            # PARENT PCIKED WITH PROBABILITY
                            p1 = snakes[i[1]]# pos of parent1
                        if pick2 in range(probability_spot, probability_spot+i[0]+1):
                            p2 = snakes[i[1]]
                        probability_spot += i[0]
                    dna1 = p2.dna[0] + p1.dna[0]
                    dna2 = p2.dna[1] + p1.dna[1]

                    #dna1 = (p2.dna[2] + p1.dna[2])/2
                    #dna2 = (p2.dna[3] + p1.dna[3])/2
                    #dna1 = (p2.dna[4] + p1.dna[4])/2
                    #dna2 = (p2.dna[5] + p1.dna[5])/2
            else:
                dna1 = numpy.random.uniform(-1.0, 1.0, 1)
                dna2 = numpy.random.uniform(-1.0, 1.0, 1)
            #time.sleep(5)

                #dna3 = numpy.random.uniform(-1.0, 1.0, 1)
                #dna4 = numpy.random.uniform(-1.0, 1.0, 1)
                #dna5 = numpy.random.uniform(-1.0, 1.0, 1)
                #dna6 = numpy.random.uniform(-1.0, 1.0, 1)

            head = turtle.Turtle()
            head.speed(0)
            head.shape("square")
            head.color("black")
            head.penup()
            head.goto(random.randint(-260,260),random.randint(-260,260))
            head.dna = [dna1, dna2]#, dna3, dna4, dna5, dna6]
            head.direction = "stop"
            head.score = 0
            head.segments = []
            snakes[x] = head#, self.brain]# idk yet
    

snake_gen_1 = Snake(25)
snake_gen_1.create("")

alive_snakes = [snake for snake in snakes]


# Snake food
foods = {}
for i in snakes:
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(200,200)
    foods[i] = food

#segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"# of Snakes: {len(alive_snakes)}  Generation: 1", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up(i):
    if snakes[i].direction != "down":
        snakes[i].direction = "up"

def go_down(i):
    if snakes[i].direction != "up":
        snakes[i].direction = "down"

def go_left(i):
    if snakes[i].direction != "right":
        snakes[i].direction = "left"

def go_right(i):
    if snakes[i].direction != "left":
        snakes[i].direction = "right"

def move(i):
    if snakes[i].direction == "up":
        y = snakes[i].ycor()
        snakes[i].sety(y + 20)

    if snakes[i].direction == "down":
        y = snakes[i].ycor()
        snakes[i].sety(y - 20)

    if snakes[i].direction == "left":
        x = snakes[i].xcor()
        snakes[i].setx(x - 20)

    if snakes[i].direction == "right":
        x = snakes[i].xcor()
        snakes[i].setx(x + 20)

# Keyboard bindings
#wn.listen()
#wn.onkeypress(go_up, "w")
#wn.onkeypress(go_down, "s")
#wn.onkeypress(go_left, "a")
#wn.onkeypress(go_right, "d")

# Main game loop
generation = 0 
while True:
    generation += 1
    alive_time = 5
    while len(alive_snakes) > 0:
        wn.update()
        ####### USE BRAIN INSTEAD #######
        for i in alive_snakes:
            ####### USE BRAIN INSTEAD #######
            #snakes[i].brain()

            #choice = random.randint(0,4)
            #if choice == 0:
            #    go_up(i)
            #elif choice == 1:
            #    go_down(i)
            #elif choice == 2:
            #    go_left(i)
            #elif choice == 3:
            #    go_right(i)
            snake_gen_1.brain(foods[i].position())


            # Check for a collision with the border
            if snakes[i].xcor()>590 or snakes[i].xcor()<-590 or snakes[i].ycor()>380 or snakes[i].ycor()<-380 or alive_time > 100:
                if alive_time > 100:
                    snakes[i].score -20
                #time.sleep(1)
                #snakes[i].goto(0,0)
                #snakes[i].direction = "stop"
                snakes[i].goto(1000,1000)

                # Hide the segments
                for segment in snakes[i].segments:
                    segment.goto(1000, 1000)

                # Clear the segments list
                snakes[i].segments.clear()
                alive_snakes.remove(i)
                snakes[i].alive_time = int(alive_time)

                # Reset the score
                score = 0

                # Reset the delay
                #delay = 0.1

                pen.clear()
                pen.write("# of Snakes: {}  Generation: {}".format(len(alive_snakes), generation), align="center", font=("Courier", 24, "normal")) 


            # Check for a collision with the food
            if snakes[i].distance(foods[i]) < 20:
                # Move the food to a random spot
                x = random.randint(-380, 380)
                y = random.randint(-380, 380)
                foods[i].goto(x,y)

                # Add a segment
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("grey")
                new_segment.penup()
                snakes[i].segments.append(new_segment)
                snakes[i].alive_time = 0

                # Shorten the delay
                #delay -= 0.001

                # Increase the score
                snakes[i].score += 10

                if score > high_score:
                    high_score = score

                pen.clear()
                pen.write("# of Snakes: {}  Generation: {}".format(len(alive_snakes), generation), align="center", font=("Courier", 24, "normal"))


            # Move the end segments first in reverse order
            for index in range(len(snakes[i].segments)-1, 0, -1):
                x = snakes[i].segments[index-1].xcor()
                y = snakes[i].segments[index-1].ycor()
                snakes[i].segments[index].goto(x, y)

            # Move segment 0 to where the snakes[i] is
            if len(snakes[i].segments) > 0:
                x = snakes[i].xcor()
                y = snakes[i].ycor()
                snakes[i].segments[0].goto(x,y)

            move(i)    

            # Check for snakes[i] collision with the body segments
            for segment in snakes[i].segments:
                if segment.distance(snakes[i]) < 20:
                    snakes[i].segments.clear()
                    alive_snakes.remove(i)
                    snakes[i].alive_time = int(alive_time)

                    for segment in snakes[i].segments:
                        segment.goto(1000, 1000)

                    # Clear the segments list
                    snakes[i].segments.clear()

                    # Reset the score
                    score = 0

                    # Reset the delay
                    delay = 0.1

                    # Update the score display
                    pen.clear()
                    pen.write("# of Snakes: {}  Generation: {}".format(len(alive_snakes), generation), align="center", font=("Courier", 24, "normal"))
        alive_time += 1

        #time.sleep(delay)
    scores = [[snakes[i].score+2, i] for i in snakes]
    scores = sorted(scores, reverse=True)

    #total_scores = 0
    #for i in scores:
    #    total_scores += i[0]
    
    #probability_spot = 0
    #pick1 = random.randint(0,total_scores)
    #pick2 = random.randint(0,total_scores)

    #for i in scores:
    #    if pick1 in [i for i in range(probability_spot, probability_spot+i[0])]: # put this is brain or something and change a ton of shit
    #        # PARENT PCIKED WITH PROBABILITY
    #        parent1 = i[1]# pos of parent1
    #    if pick2 in [i for i in range(probability_spot, probability_spot+i[0])]:
    #        parent2 = i[1]


    

    # GENETIC ALGORITHM TIME!!!
    # have probablility of selection be in 
    # relation to the score/ fitnesses of the snakes
    # add all scores together
    # pick randint(0,fitness_sum)
    # if randint is in a cetain section than whoever
    # gets it

    # incentive time between apple gets, but 
    # not a ton

    snake_gen_1.create(scores)

    alive_snakes = [snake for snake in snakes]

wn.mainloop()