import random
import curses
high = 0
file = open('hs.txt','r')
for l in file:
    high = int(l.strip())
file.close()
score = 0

#initial cusrse for the initialize library and return a window object
snk = curses.initscr()
#set curse to invisible
curses.curs_set(0)
#set the height and width of the window from max dimensions
seth, setw = snk.getmaxyx()
#create a new window
w = curses.newwin(seth,setw,0,0)
#taking input from the suer
w.keypad(1)
#refresh screen every 100ms
w.timeout(100)

#set initial position of snake
snake_x = setw/5
snake_y = seth/5
#create the initial snake and food
snake = [[snake_y,snake_x],[snake_y,snake_x-1],[snake_y,snake_x-2]]
food = [seth/2,setw/2]
w.addch(int(food[0]),int(food[1]), curses.ACS_DIAMOND)

key = curses.KEY_DOWN
#Loop for the game l    ogic
while True:
    #taking the input and chaning only when thers's another prompt
    next_key = w.getch()
    key = key if next_key == -1 else next_key
    #boundary conditions if snake hits a wall or bites itself
    if snake[0][0] in [0, seth]  or snake[0][1] in [0, setw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()
    #creating a new head
    new_head = [snake[0][0], snake[0][1]]
    #create movement
    if key == curses.KEY_DOWN:
        new_head[0]+= 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    #add movement
    snake.insert(0, new_head)
    #snake eats the diamond
    if snake[0] == food:
        food = None
        score+=1
        if high<score:
            high = score
            file = open('hs.txt','w')
            file.write(str(high))
            file.close()
        while food is None:
            nf = [
                random.randint(1, seth-1),
                random.randint(1, setw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_DIAMOND)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')
    #snake body
    w.addstr(0, 0, "Score:"+str(score)+ "  High Score:"+str(high)+"",
              curses.A_REVERSE)
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_BLOCK)
