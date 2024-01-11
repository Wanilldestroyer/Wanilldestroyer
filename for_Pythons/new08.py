from operator import pos
from matplotlib.patches import ArrowStyle
import matplotlib.pyplot as plt
import networkx as nx
import sys
stdout = sys.stdout
G = nx.Graph()  
# ������ ������ �����

try:
    sys.stdout = open("C:\\Python3_11\\file04.py", 'r')
    a = sys.stdout.readlines()
finally:
    # ��������� file
    sys.stdout.close()
    sys.stdout = stdout
# ���������� ������ ����� (ID �����)

nodes=(4, 6)
# ���������� ������ ����
# ������ ��������, ������ �� ������� ������������ �����
# ������ (id_1, id_2) ��������, ��� ���� id_1 � id_2 ��������� ������
edges = [(1, 2), (1, 3), (3, 4), (2, 5), (5, 7), (6, 7)]

# ��������� ���������� � ������ �����
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_nodes_from(nodes)
G.add_node(5)
G.add_node(7)
G.add_node(4,6)
G.add_edges_from(edges)


# ������ ���� � ���������� ���
pos = nx.circular_layout(G)

options = {
    'node_color': 'red',     # color of node, spectral color for random colors!!!
    'node_size': 3500,          # size of node
    'width': 1,                 # line width of edges
    'arrowstyle': '-|>',        # array style for directed graph
    'arrowsize': 18,            # size of arrow
    'edge_color':'blue',        # edge color
}

nx.draw(G, pos, with_labels = True,arrows=True, **options)
plt.show()



