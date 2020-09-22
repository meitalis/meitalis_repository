import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_node("a")
G.add_nodes_from(["b","c"])

G.add_edge(1,2)
edge = ("d", "e")
G.add_edge(*edge)
edge = ("a", "b")
G.add_edge(*edge)

print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())

#Nodes of graph:
['a', 1, 'c', 'b', 'e', 'd', 2]
#Edges of graph:
[('a', 'b'), (1, 2), ('e', 'd')]

# adding a list of edges:
G.add_edges_from([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])


nx.draw_networkx(G,arrows=True,node_size=1000, node_color='#00b4d9')#nx.draw(G)
plt.grid('on')
#plt.axis('on')
#plt.savefig("simple_path.png") # save as png

plt.show() # display



#G = nx.path_graph(4)
#nx.draw_networkx(G)
#plt.grid('on')
#plt.show()