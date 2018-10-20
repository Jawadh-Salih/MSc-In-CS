from random import randint, random, shuffle
from node import Node
from graph import Graph
from utils import cum_prob_dist, create_nodes, get_prob_dict, create_init_graph, create_edge, cal_degree, get_random_user, get_current_degree_probs, insertEdge, get_random_max_prob_movie, plot_degree_distibution, get_alpha_for_degree_dist, tot_degree, wieghted_choice

import numpy
# Create some unique labels.
# Assuming that we have got some defined Nodes for Movies and Users.
# What is the data structure for Movies set. It should be a set, Users should be a set.
# Then both the sets has to be interacted with each other as dictionery data structure. 
#  This will be a dynamic dictionery where with the time, new M,U pairs are combined. 

M = create_nodes("M", 1000) # Should create a dictionary
U = create_nodes("U", 1000)
G = Graph(M, U)
create_init_graph(M, U, G)

G.print_graph()
print([m.degree for m in M])
# Created graph should be connected. 
# need to define a probability.
# need to see whether nodes get upon it.


print('Initial Graph is created') # This initial Graph is a collection of Edges where pair of nodes from M, U are linked 
G.print_degree_dist(M)
G.print_graph()
cum_prob_dist(M)

for i in range(10000) :
    u = get_random_user(U)

    for m in M:
        if (m.cum_prob > random()) :
            # add an edge to k
            newU = Node(0, 'U' + str(len(U)))
            U.append(newU)
            G.insert_edge(newU, m)
            cum_prob_dist(M)
        
            break
        else :
            G.insert_edge(u, m)
            cum_prob_dist(M)
# for i in range(10000) :
    
        # m has to be chosen with the preference..
# Choose a Node from the set where the pref_prob is greater or equal.
# G.print_graph()
G.print_degree_dist(M)


# print(sorted(get_current_degree_probs(M,  tot_degree(M))))
plot_degree_distibution(M)

