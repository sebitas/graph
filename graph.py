import osmnx as ox
place = 'AQP, Peru'
gdf = ox.gdf_from_place('AQP, Peru')
# data
G = ox.graph_from_place(place, network_type='drive')
G_projected = ox.project_graph(G)
# save street network as GraphML file
ox.save_graphml(G_projected, filename='network.graphml')
G2 = ox.load_graphml('network.graphml')
fig, ax = ox.plot_graph(G2)

