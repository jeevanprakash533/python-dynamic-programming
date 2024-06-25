map=[[0,10,35,40],
     [10,0,20,25],
     [35,20,0,30],
     [40,25,30,0]]
def findway(visited,pos):
    if len(visited)==len(map):
        return map[pos][0]
    mindis=999   #taking an random max number compared to all  or we can take as "mindis=float('inf')""
    for city in range(len(map)):
        if city not in visited:
            newvisited=visited+[city]
            newdistance=map[pos][city]+findway(newvisited,city)
            mindis=min(mindis,newdistance)
    return mindis
visited=[0]
print(findway(visited,0))
