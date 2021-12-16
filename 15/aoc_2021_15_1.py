import helper
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pylab

data = [
    '1163751742',
    '1381373672',
    '2136511328',
    '3694931569',
    '7463417111',
    '1319128137',
    '1359912421',
    '3125421639',
    '1293138521',
    '2311944581',
]

data = helper.get_puzzle_input(d=15, y=2021)

axis_0 = len(data)
axis_1 = len(data[0])
data = [int(x) for x in ''.join(data)]
data = np.array(data).reshape((axis_0, axis_1))

start = (0, 0)
finish = (data.shape[0] - 1, data.shape[1] - 1)


big_nums_mask = data > 7
data = np.where(big_nums_mask, 9999, data)

weights_arr = data / np.linalg.norm(data)
print(weights_arr)
weights_dict = {}
for r, row in enumerate(weights_arr):
    for c, col in enumerate(row):
        try:
            # Horizontal weights
            weights_dict[((r, c), (r, c+1))] = weights_arr[r, c+1]
            # Vertical weights
            weights_dict[((r, c), (r+1, c))] = weights_arr[r+1, c]
        except IndexError:
            pass

nxgrid = nx.grid_2d_graph(data.shape[0], data.shape[1])
nx.set_edge_attributes(nxgrid, weights_dict, 'weight')

# paths = nx.all_shortest_paths(nxgrid, start, finish, weight='weight')#, method='bellman-ford')

risks = []
# calc_all_paths = list(nx.all_shortest_paths(nxgrid, start, finish, weight='weight', method='dijkstra'))
# foo = [p for p in calc_all_paths]
# all_paths = []
# for fo in foo:
#     test_arr = np.full(data.shape, np.NaN, dtype='float')
#     for coord in fo:
#         row = coord[0]
#         col = coord[1]
#         test_arr[row, col] = data[row, col]
#     risk = test_arr[np.logical_not(np.isnan(test_arr))][1:].sum()
#     all_paths.append(test_arr)
#     if risk not in risks:
#         risks.append(risk)


astar = nx.shortest_path(nxgrid, start, finish, weight='weight')
test_arr = np.full(data.shape, np.NaN, dtype='float')
for coord in astar:
    test_arr[coord] = data[coord]

risk = test_arr[np.logical_not(np.isnan(test_arr))][1:].sum()
print(risk)

# plt.figure(figsize=(6,6))
# pos = {(x,y):(y,-x) for x,y in nxgrid.nodes()}
# nx.draw(nxgrid, pos=pos,
#         node_color='lightgreen',
#         # with_labels=True,
#         node_size=10)


# print(nxgrid.edges(data=True))
# test = [edge_attr['weight'] ]

# for (node1, node2, edge_attr) in nxgrid.edges(data=True):
#     print(node1, node2, edge_attr.get('weight'))

# all_weights = []
# for (node1,node2,data) in nxgrid.edges(data=True):
#     all_weights.append(data['weight']) #we'll use this when determining edge thickness
# unique_weights = list(set(all_weights))
# for weight in unique_weights:
#     #4 d. Form a filtered list with just the weight you want to draw
#     weighted_edges = [(node1,node2) for (node1,node2,edge_attr) in nxgrid.edges(data=True) if edge_attr['weight']==weight]
#     width = weight
#     nx.draw_networkx_edges(nxgrid,pos,edgelist=weighted_edges,width=width)


plt.show()

# pos = nx.spring_layout(nxgrid)
# pylab.figure(2)
# nx.draw(nxgrid, pos)
# edge_labels=dict([((u,v,),d['weight'])
# for u,v,d in nxgrid.edges(data=True)])
# nx.draw_networkx_edge_labels(nxgrid,pos,edge_labels=edge_labels)
# pylab.show()
# for path in calc_all_paths:
#     foo.append(path)
#     # path = nx.dijkstra_path(nxgrid, start, finish, weight='weight')
#     test_arr = np.full(data.shape, np.NaN, dtype='float')
#     for coord in path:
#         row = coord[0]
#         col = coord[1]
#         test_arr[row, col] = data[row, col]
#     risk = test_arr[np.logical_not(np.isnan(test_arr))][1:].sum()
#     risks.append(risk)
# print(risks)
#
# print(len(all_paths))
# fig, ax = plt.subplots()
#
# for arr in all_paths:
#     plt.imshow(arr)
#
# plt.show()
# print(len(foo))
# print(foo[0])
# path = nx.dijkstra_path(nxgrid, start, finish, weight='weight')
# test_arr = np.full(data.shape, np.NaN, dtype='float')
# for coord in path:
#     row = coord[0]
#     col = coord[1]
#     test_arr[row, col] = data[row, col]
#
# risk = test_arr[np.logical_not(np.isnan(test_arr))][1:].sum()

# print(risk)
