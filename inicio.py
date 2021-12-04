wall = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
start = ((0,0))
exit = ((4,4))
# maze shape
#maze1 = [" ","X","X","X","X"]
#maze2 = [" ","X"," "," "," "]
#maze3 = [" ","X"," ","X"," "]
#maze4 = [" "," "," ","X"," "]
#maze5 = ["X","X","X","X"," "]


lab=[]
def mazecreation():
        maze = []
        for i in range(0,5): #line
                for j in range(0,5): #column
                                      
                        if tuple([i,j]) in wall:
                                maze.append("X")
                        else:
                                maze.append(" ")
                lab.append (maze)
                maze = []
mazecreation()
  
for x in lab:
    print(" ".join(x))

x = 0
y = 0
direction = "down"
"""
def mazemovements(x1,y1, direction1):
        if (x1,y1) in wall:  # down
                x1 = x1 + 1  
                if (x1,y1) in wall:  # right
                        x1 = x1 - 1 
                        y1 = y1 + 1
                        direction1 = "right"
                        if (x1, y1) in wall: # up
                                y1 = y1 - 1 
                                x1 = x1 - 1
                                direction1 = "up"
        return x1, y1, direction1
                

#while x < 4 and y < 4:
           
(x,y, direction)=mazemovements(x,y, direction)
print (x, y, direction)

print("You win!!")
"""

def downmovement(x1, y1, direction1):
        x1 = x1 + 1
        y1 = y1
        direction1 = "down"
        return x1, y1, direction1

def rightmovement(x2, y2, direction2):
        x2 = x2 - 1 
        y2 = y2 + 1
        direction2 = "right"
        return x2, y2, direction2


def upmovement(x3, y3, direction3):
        y3 = y3 - 1 
        x3 = x3 - 1
        direction3 = "up"
        return x3, y3, direction3

while direction == "down":
        movement1 = downmovement(x, y, direction)
        if movement1 in wall:
                movement2 = rightmovement(x, y, direction)
while direction == "right":
        movement2 = rightmovement(x, y, direction)
        if movement2 in wall:
                movement3 = upmovement(x, y, direction)
while direction == "up":
        movement3 = upmovement(x, y, direction)
        if movement3 in wall:
                movement2 = rightmovement(x, y, direction)
if x == 4 and y == 4:
        print("You win")
