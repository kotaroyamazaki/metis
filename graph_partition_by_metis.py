import networkx as nx
import metis 
import numpy
import sys

if __name__ == '__main__':
    args = sys.argv
    if len(args) >= 4:
        if args[2].isdigit() and args[3].isdigit():
            fname = args[1]
            nodeNum = int(args[2])
            npart = int(args[3])
        else:
            print('Error! Argument is not digit')
    else:
        print('Error! Arguments are too short.')
        print('Usage: {} [input file] [nodes num] [partition num]'.format(sys.argv[0]))
        quit()

G = nx.Graph()
for l in open(fname).readlines():
    data = l[:-1].split(' ')
    G.add_edge(int(data[0]), int(data[1]), weight=int(data[2]))

nodes = numpy.arange(nodeNum)
G.add_nodes_from(nodes)

(edgecut, parts) = metis.part_graph(G, npart)

print('edgec: ',edgecut)           # The number of cut edges.
print('parts: ',parts)             # Display the number of nodes after partition.
