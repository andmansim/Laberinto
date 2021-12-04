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
        x2 = x2 
        y2 = y2 + 1
        direction2 = "right"
        return x2, y2, direction2


def upmovement(x3, y3, direction3):
        y3 = y3
        x3 = x3 - 1
        direction3 = "up"
        return x3, y3, direction3

fin = False
while fin != True:
        
        while direction == "down":
                x,y,direction= downmovement(x, y, direction)
        
                if (x,y) in wall:
                        x = x - 1
                        x,y,direction = rightmovement(x, y, direction)
                
                        if (x,y) in wall:
                                y = y - 1
                                x,y,direction = upmovement(x, y, direction)
                                print(x,y,direction) 
                        else:
                                print(x,y,direction)
                else:
                        print(x,y,direction)  
                        
        while direction == "right":
                x,y,direction = rightmovement(x, y, direction)
        
                if (x,y) in wall:
                        y = y - 1
                        x,y,direction = downmovement(x, y, direction)
                
                        if (x,y) in wall:
                                x = x - 1
                                x,y,direction = upmovement(x, y, direction)
                                print(x,y,direction) 
                        else:
                                print(x,y,direction)
                else:
                        print(x,y,direction)
                
        while direction == "up":
                x,y,direction = upmovement(x, y, direction)
        
                if (x,y) in wall:
                        x = x + 1
                        x,y,direction = rightmovement(x, y, direction)
                
                        if (x,y) in wall:
                                y = y - 1
                                x,y,direction = downmovement(x, y, direction)
                                print(x,y,direction) 
                        else:
                                print(x,y,direction)
                else:
                        print(x,y,direction)
                
if x == 4 and y == 4 :
        fin = True
        print("You win")
        direction = " "
