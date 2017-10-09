import osmnx as ox, networkx as nx
G = ox.load_graphml('network.graphml')
# define a lat-long point, create network around point, define origin/destination nodes
origin_node = list(G.nodes())[2]
destination_node = list(G.nodes())[-1]
# find the route between these nodes then plot it
route = nx.shortest_path(G, origin_node, destination_node)
count = 0
for i in list(route):
  count += 1
print(count)
ox.plot_graph_route(G,route)