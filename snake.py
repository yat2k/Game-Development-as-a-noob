import random
import curses

s = curses.initscr()                               #initialize the screen , s is for screen
curses.curs_set(0)                                 #initializes the middle of the screen to (0,0)
sh,sw = s.getmaxyx()                               #full screen game, sh - screen height, sw - screen width
w = curses.newwin(sh,sw,0,0)                       #pop up new window
w.keypad(1)                                        #accepting kewboard input
w.timeout(100)                                     #clearing screen and opening another frame (thats how characters move), 100 ms
snk_x = sw/4                                       #initializing snake head's x coordinate
snk_y = sh/2                                       #initializing snake head's y coordinate
snake=[                                            # snake body
    [snk_y,snk_x],
    [snk_y,snk_x-1],
    [snk_y,snk_x-2]
]
food = [sh/2,sw/2]                                 # food coordinates
w.addch(int(food[0]),int(food[1]),curses.ACS_PI)   # sets the food to pi character

key = curses.KEY_RIGHT                             # KEY_RIGHT is the right arrow key, after we press it it will go in while
while True:
    next_key = w.getch()                           # if we dont press any key it will give -1
    key = key if next_key == -1 else next_key
    
    if snake[0][0] in [0,sh] or snake[0][1] in [0,sw] or snake[0] in snake[1:]:   # checking if head collides with walls or itself
        curses.endwin()
        quit()
    new_head = [snake[0][0],snake[0][1]]           #initializing a new head to be added                                    
    
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
        
    snake.insert(0,new_head)
    
    if snake[0] == food:
        food = None
        while food is None:
            nf=[random.randint(1,sh-1),
                random.randint(1,sw-1)]
            food = nf if nf not in snake else None
        w.addch(food[0],food[1],curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]),int(tail[1]),' ')
        
    w.addch(int(snake[0][0]),int(snake[0][1]),curses.ACS_CKBOARD)
    
        

        

    