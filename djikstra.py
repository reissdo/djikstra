import numpy as np

def createGraph(nNodes,maxWeight = 10,probab = 0.8):
    """
    +number of nodes [int]
    
    creates random adjacency matrix
    
    -adjacency matrix [numpy array]
    """
    
    matrix = np.random.randint(1, maxWeight + 1, size=(nNodes, nNodes))
    mask = np.random.rand(nNodes, nNodes) < probab
    matrix = matrix * mask
    np.fill_diagonal(matrix, 0)

    return matrix

def djikstra(adjMat,startNode,endNode):
    """
    +adjacency matrix [numpy array]
    +start node [int]
    +end node [int]
    
    finds the shortes path between start node and end node
    
    -path from start node to end node [list]
    """
    
    if adjMat.shape[0] != adjMat.shape[1]:
        print("error: number of rows != number of cols")
        print(adjMat.shape)
        return
    
    if startNode >= adjMat.shape[0] or endNode >= adjMat.shape[0]:
        print("error: start node or end node does not exist")
        print("start node: ",startNode,"\nend node: ",endNode)
        return
    
    table = np.zeros((adjMat.shape[0],3),dtype=int) #list for every node: [wasVisited,cost,previousNode]
    
    for row in table:
        row[1] = 10**10
        row[2] = -1

    table[startNode][1] = 0 
    
    #start djikstra
    for i in range(adjMat.shape[0]):
        
        notVisited = []
        for i in range(table.shape[0]):
            if table[i][0] == 0:
                notVisited.append([i,table[i][1]])
        
        currentNode = min(notVisited,key=lambda n: n[1])[0]
        table[currentNode][0] = 1
        
        for j in range(adjMat[currentNode].shape[0]):
            if adjMat[currentNode][j] == 0 or table[j][0] == 1:
                continue
            else:
                cost = table[currentNode][1] + adjMat[currentNode][j]
                if cost < table[j][1]:
                    table[j][1] = cost
                    table[j][2] = currentNode
                         
    path = []
    currentNode = endNode
    path.append(currentNode)
    
    while currentNode != startNode:
        if table[currentNode][2] == -1:
            print("path from start node to end node is not possible")
            return
        else:
            nextNode = table[currentNode][2]
            path.append(nextNode)
            currentNode = nextNode
    path.reverse()
    return path


adjMat = createGraph(20,10,0.1)
print(adjMat)
startNode = 0
endNode = 19

path = djikstra(adjMat,startNode,endNode)
print(path)