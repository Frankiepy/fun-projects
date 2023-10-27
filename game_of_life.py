def count(lst, x,y):
    count = 0
    for point in lst:
        if point in [(x-1,y),(x+1,y),(x,y-1),(x,y+1),(x+1,y+1),(x-1,y+1),(x+1,y-1),(x-1,y-1)]:
            count += 1
    return count
                
grid = [(0,0),(0,2),(1,0),(1,1),(2,1),
        (-4,-4),(-4,-3),
        (-3,-4),(-3,-3)
        ]

def game_of_life(lst):
    new_grid = []
    xs = []
    ys = []
    for (x,y) in lst:
        num = count(lst, x,y)
        if num == 2 or num == 3:
            new_grid.append((x,y))
        xs.append(x)
        ys.append(y)

    visual = []
    old_visual = []

    for x in range(min(xs)-1,max(xs)+2):
        temp = []
        old_temp = []
        for y in range(min(ys)-1,max(ys)+2):
            if (x,y) not in lst:
                old_temp.append(" ")
                num2 = count(lst, x,y)
                if num2 == 3:
                    new_grid.append((x,y))
                    temp.append("#")
                else:
                    temp.append(" ")
            else:
                if (x,y) in new_grid:
                    temp.append("#")
                else:
                    temp.append(" ")
                old_temp.append("#")
        old_visual.append(old_temp)
        visual.append(temp)
    #for i in old_visual:
    #    print(i)
    for i in visual:
        print(i)
    return new_grid
    
for i in range(0,1000000):
    grid = game_of_life(grid)
    print(grid)