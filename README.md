# graphs_dijkstra_algorithm
Simple graph implementation with Dijkstra's optimal path algorithm.

### About Dijkstra Algorithm
Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks. It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published three years later.
[Read more on Wikipedia...](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

### Usage

**Create graph**
```Python
g = Graph()
```

**Add nodes to graph**
```Python
g.add_nodes(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'Z'])
```

**Delete node(s) from graph**
```Python
g.del_nodes(['Z'])
```

**Add edges to graph**
If some of the affected nodes does not exist, it will be added automatically with new edge
```Python
g.add_edges(
  [
    ('A', 'B', 2), ('A', 'C', 5), ('A', 'D', 1), ('A', 'E', 6), ('B', 'C', 3), 
    ('C', 'D', 2), ('C', 'G', 1), ('D', 'F', 2), ('E', 'F', 2), ('F', 'G', 3)
  ]
)
```

**Display graph**
```Python
g.display()
A
 -  C ( 5 )
 -  D ( 1 )
 -  B ( 2 )
 -  E ( 6 )

G
 -  C ( 1 )
 -  F ( 3 )

F
 -  G ( 3 )
 -  D ( 2 )
 -  E ( 2 )

D
 -  A ( 1 )
 -  C ( 2 )
 -  F ( 2 )

B
 -  A ( 2 )
 -  C ( 3 )

C
 -  A ( 5 )
 -  G ( 1 )
 -  D ( 2 )
 -  B ( 3 )

E
 -  A ( 6 )
 -  F ( 2 )
```

**Run Dijkstra algorithm on graph's one selected node (source)**
```Python
>>> previous_steps, cheapest_paths = g.dijkstra('A')
>>> 
>>> previous_steps
{'C': 'D', 'B': 'A', 'D': 'A', 'E': 'F', 'F': 'D', 'G': 'C', 'A': None}
>>> 
>>> cheapest_paths
{'C': 3, 'B': 2, 'D': 1, 'E': 5, 'F': 3, 'G': 4, 'A': 0}
```

**Get optimal path on graph from node (source) to an other node (target)**
```Python
>>> cost, length, steps = g.optimal_path('A', 'G')
>>> 
>>> cost
4
>>> 
>>> length
3
>>> 
>>> steps
['A', 'D', 'C', 'G']
```
