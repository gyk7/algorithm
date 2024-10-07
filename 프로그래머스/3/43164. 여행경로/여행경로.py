from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    
    for start, end in tickets :
        graph[start].append(end)
        
    for start in graph :
        graph[start].sort(reverse = True)
    route = []
    def dfs(node):
        while graph[node] :
            next_node = graph[node].pop()
            dfs(next_node)
        route.append(node)     
        
    dfs('ICN')
    return route[::-1]
        