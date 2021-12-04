# Laberinto

Mi dirección de GitHub par el juego del laberinto es el siguiente: [GitHub](https://github.com/andmansim/Laberinto.git)

https://github.com/andmansim/Laberinto.git
En la primera parte hemos realizado el inicio de un laberinto, marcando los muros y los pasillos. En la segunda, hemos puesto las instrucciones necesarias para resolverlo y que nos muestre los pasos que ha tenido que realizar.

![El diagrama de flujo que hemos usado para este proyecto es el siguiente:] ()

```
wall = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
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
