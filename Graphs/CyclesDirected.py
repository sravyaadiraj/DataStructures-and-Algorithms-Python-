
#Time Complexity O[E+V]
#Space complexity O[E]
#Approach-->DFS

def cycle_detected(Graph_Input):
    #Creted dictioanry to track color
    #Initially for all nodes it is white(unvisited)
    colr_dcit={i:"white" for i in Graph_Input}
    path=[False]
    for u in Graph_Input:
        #if node is unvisited,call recursive function
        if colr_dcit[u]=="white":
            helper(Graph_Input,u,colr_dcit,path)
        if path[0]:
            break
    return path[0]
def helper(g,u,colr_dcit,path):
    if path[0]:
        return
    #inOw the node is visited and change the color to grey
    colr_dcit[u]="grey"
    #for all the neighbors to the node
    for v in g[u]:
        #if the neighbor is alreadfy visited then change the color to grey and hence it is cyclic
        if colr_dcit[v]=="grey":
            path[0]=True
            return
        if colr_dcit[v]=="white":
            helper(g,v,colr_dcit,path)
    colr_dcit[u]="black"
graph_example_1 = { 0 : [1],
                    1 : [2],
                    2 : [3],
                    3 : [4],
                    4 : [5] }

print("Result is    :   ",cycle_detected(graph_example_1))

    

    

