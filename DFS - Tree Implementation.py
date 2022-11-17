graph = {
  's' : ['a', 'b'],
  'a' : [],
  'b' : ['c', 'd'],
  'c' : [],
  'd' : ['e', 'f'],
  'e' : [],
  'f' : ['g', 'h'],
  'g' : [],
  'h' : ['i', 'j'],
  'i' : [],
  'j' : []
}

visited = set() 

def dfs(visited, graph, node):  
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print("Following is the Depth-First Search")
dfs(visited, graph, 's')