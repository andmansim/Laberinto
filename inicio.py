
wall = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

#maze1 = [" ","X","X","X","X"]
#maze2 = [" ","X"," "," "," "]
#maze3 = [" ","X"," ","X"," "]
#maze4 = [" "," "," ","X"," "]
#maze5 = ["X","X","X","X"," "]

maze1 = []
maze2 = []
maze3 = []
maze4 = []
maze5 = []
def mazecreation():
        for i in range(0,5):
                
                if tuple([0,i]) in wall:
                        maze1.append("X")
                else:
                        maze1.append(" ")
                        
                if tuple([1,i]) in wall:
                        maze2.append("X")
                else:
                        maze2.append(" ")
                if tuple([2,i]) in wall:
                        maze3.append("X")
                else:
                        maze3.append(" ")
                if tuple([3,i]) in wall:
                        maze4.append("X")
                else:
                        maze4.append(" ")
                if tuple([4,i]) in wall:
                        maze5.append("X")
                else:
                        maze5.append(" ")
mazecreation()


lab=[]
lab.append (maze1)
lab.append (maze2)  
lab.append (maze3)
lab.append (maze4)
lab.append (maze5)    
for x in lab:
    print(" ".join(x))

                
        
