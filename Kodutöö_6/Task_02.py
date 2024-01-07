# Analüüs:
# 
# Ajakomplekssus: Ajakomplekssus sõltub graafi struktuurist. Halvimal juhul, kui graaf on tugevalt harunenud, võib olla 
# O(V+E), kus V on sõlmede arv ja E on servade arv.
# 
# Ruumikomplekssus: Ruumikomplekssus sõltub sõlmede külastatud hulgast, seega O(V).
# DFS on sügavust esmalt otsiv algoritm, mis kasutab rekursiooni, mistõttu võib see tarbida rohkem mäluruumi, kui graaf on sügav. 
# Aja- ja ruumikomplekssus sõltub suuresti graafi struktuurist.



def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Graafi esitamine dictionarinna.
example_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

# Algussõlm
start_node = 'A'

# Külastatud sõlmed
visited_nodes = set()

print("DFS traversal:")
dfs(example_graph, start_node, visited_nodes)
