from random import randint, random
from utils import create_nodes, create_zipf_nodes, get_lower_degree_Node, get_zipf_curve, create_init_graph, tot_degree, plot_degree_distibution, get_random_user, cum_prob_dist
from graph import Graph
import matplotlib.pyplot as plt

import numpy as np


jet= plt.get_cmap('jet')
colors = iter(jet(np.linspace(0,1,200)))
# Create a set of M nodes
m_nodes = randint(900, 1000)
M = create_nodes('M', m_nodes)
Z = create_nodes('Z', m_nodes)
# Create a set of U nodes
U = create_nodes('U', randint(9000, 10000))

# Now there isn't a competition. So Movies can be viewed by infinite number of users.
# This is against the given definition of Zipf's Law, which states there is scarcity of the sharing resources.
# But for our scenario we have used time as a scarce resources. 

# Now create a Graph with set of nodes connected in a bipartite way
G = Graph(M, U)
create_init_graph(M, U, G)
G.print_degree_dist(M)
L_m = list()
# if degree of U is 0, then it will be connected to the most degree node.
for i in range (20000) : # we are going to do operations 100 times to see what will happen to the network
    # get a random user. For this I didn't consider the probabilities of User Nodes.
    u = get_random_user(U)
    if (u.degree in range(0,3)) : # User is a new one. If this is the case.
        # connect u with one of the most degree M nodes. 
        cum_prob_dist(M)
        for m in M :
            if (m.cum_prob > random()) : 
                G.insert_edge(m, u)
                cum_prob_dist(M)
                break
    else:
        # now this can connect to any other node.
        print("Else")
        m = get_lower_degree_Node(L_m, M, 10)
        G.insert_edge(m, u)
        cum_prob_dist(M)

    # if (i % 2000 == 0) :
    #     plot_degree_distibution(plt, M, next(colors))


        

# D_m = G.gt_degree_dist(M)
G.print_degree_dist(M)

max_degree = max(m.degree for m in M)
create_zipf_nodes(Z, max_degree)
length_m = len(M)
plot_degree_distibution(plt, Z, next(colors))
plot_degree_distibution(plt, M, next(colors))

plt.show()
# plot_degree_distibution(U)