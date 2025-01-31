import numpy as np
import math

adjMat=         [[0,1,0,4,3,0],
                 [1,0,5,0,1,0],
                 [0,5,0,2,1,0],
                 [4,0,2,0,2,0],
                 [3,1,1,2,0,1],
                 [0,0,1,0,0,0]]
startNode = 1

def djikstra(adjMat,startNode):
    if(adjMat.shape[0] != adjMat.shape[1]):
        print("error: number of rows != number of cols")
        print(adjMat.shape)
        return
    
    table = np.zeros((adjMat.shape[0],3))
    
    for row in table:
        row[1] = math.inf
        row[2] = -1

    table[startNode][1] = 0 
    
    for i in range(adjMat.shape[0]):
        
    
    print(table)


    return




djikstra(np.asarray(adjMat),startNode)