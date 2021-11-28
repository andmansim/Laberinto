
wall = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

space = ((1,0), (1,2), (1,3), (1,4), (2,0), (2,2), (2,4), (3,0), (3,1), (3,2), (3,4))


maze1 = [" ","X","X","X","X"]
maze2 = [" ","X"," "," "," "]
maze3 = [" ","X"," ","X"," "]
maze4 = [" "," "," ","X"," "]
maze5 = ["X","X","X","X"," "]
lab=[]
lab.append (maze1)
lab.append (maze2)  
lab.append (maze3)
lab.append (maze4)
lab.append (maze5)    
for x in lab:
    print(" ".join(x))

                
        
