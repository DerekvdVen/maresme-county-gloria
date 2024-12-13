from pathlib import Path

import osmnx as ox

data_path = Path(__file__).parent / "data"
graph = ox.graph_from_point((41.665, 2.74), 5000)

nodes, edges = ox.graph_to_gdfs(graph)
edges.to_file(str(data_path / "roads.geojson"), driver="GeoJSON")
