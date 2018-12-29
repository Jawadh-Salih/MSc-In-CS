from random import randint, random, shuffle
from node import Node
from graph import Graph
from utils import sort_by_degree, create_zipf_nodes, cumulative_prob_dist, create_nodes, get_prob_dict, create_init_graph, create_edge, cal_degree, get_random_user, get_current_degree_probs, insertEdge, get_random_max_prob_movie, plot_degree_distibution, get_alpha_for_degree_dist, tot_degree, wieghted_choice

import numpy as np
import matplotlib.pyplot as plt
# Create some unique labels.
# Assuming that we have got some defined Nodes for Movies and Users.
# What is the data structure for Movies set. It should be a set, Users should be a set.
# Then both the sets has to be interacted with each other as dictionery data structure. 
#  This will be a dynamic dictionery where with the time, new M,U pairs are combined. 
m_nodes = randint(900, 1000)

M = create_nodes("M", m_nodes) # Should create a dictionary
U = create_nodes("U", 10000)
Z = create_nodes('Z', m_nodes)

G = Graph(M, U)
create_init_graph(M, U, G)

# G.print_graph()
# Created graph should be connected. 
# need to define a probability.
# need to see whether nodes get upon it.


print('Initial Graph is created') # This initial Graph is a collection of Edges where pair of nodes from M, U are linked 
G.print_degree_dist(M)
cumulative_prob_dist(M)
cumulative_prob_dist(U)

# Barabasi ALbert Model. 
def BA_Model() :
    for i in range(10000) :
        u = get_random_user(U)

        for m in M:
            if (m.cumulative_prob > random()) :
                # add an edge to k
                newU = Node(0, 'U' + str(len(U)))
                U.append(newU)
                G.insert_edge(newU, m)
                cumulative_prob_dist(M)
            
                break
            else :
                G.insert_edge(u, m)
                cumulative_prob_dist(M)

# Below this, I have implemented the Model proposed in the Paper Named Evolving Model of Online Bipartite Network

# Scenario for adding a new User to the Network 
def add_new_user(G, U, M, num, val) :
    # should add this user to m nodes from M 
    # preserving the preferencial attachment behavior
    user = Node(0, 'U' + str(len(U)))
    for x in range(num) :
        for m in M : # 1000 * 50,000,000
            # val (is a random value) will fit into the bigger span of cumulative probability line.
            if (m.cumulative_degree > val) :
                U.append(user)
                G.insert_edge(user, m)
                cumulative_prob_dist(M)
                break

# Scenario for adding a new Movie (Object) to the Network
def add_new_movie(G, U, M, num, val) :
    newM = Node(0, 'M' + str(len(M)))
    # Add a new Object
    for x in range(num):
        for u in U : 
            if (u.cumulative_prob > val) :
                M.append(newM)
                G.insert_edge(u, newM)
                cumulative_prob_dist(U)
                break 

# Scenario for adding an edge (Using existing nodes) randomly to the network
def add_edge_to_graph(G, U, M, num, val) :
    # Adding an edge to the exisiting Graph.
    for x in range(num):
        u = get_random_user(U) 
        # val = random()
        for m in M :
            if (m.cumulative_prob > val) :
                G.insert_edge(u, m)
                cumulative_prob_dist(M)
                break

# Scenario for adding an edge (Using existing nodes) with preferential attachment to the network
def add_edge_with_pref(G, U, M, num, val):
    # Adding an edge with pref prob

    tempM = None
    tempU = None
    for x in range(num) :
        for m in M :
            if (m.cumulative_prob > val) :
                tempM = m
                break

        for u in U :
            if (u.cumulative_prob > val) :
                tempU = u
                break
        
        G.insert_edge(tempU, tempM)
        cumulative_prob_dist(M)
        cumulative_prob_dist(U)

# Implementation of the Model proposed in the paper. 
def Pref_Model(iters) :
    for x in range(iters) :
        val = random()
        add_new_user(G, U, M, 1, val) #C randint(1,10))
        val = random()
        add_new_movie(G, U, M, 1, val) #randint(1,10))
        val = random()
        add_edge_to_graph(G, U, M, 1, val) #randint(1,10))
        val = random()
        add_edge_with_pref(G, U, M, 1, val) # randint(1,10))

Pref_Model(100) # Model to  10000 iterations to implement the simualtion.


jet= plt.get_cmap('jet')
colors = iter(jet(np.linspace(0,1,200)))
max_degree_m = max(m.degree for m in M)
max_degree_u = max(u.degree for u in U)
# create_zipf_nodes(Z, max_degree, 2)
# plot_degree_distibution(plt, Z, next(colors))
create_zipf_nodes(Z, max_degree_m, 1) # creating Zipfs nodes as the reference 
plot_degree_distibution(plt, Z, next(colors))
G.print_degree_dist(sort_by_degree(M))
m1 = Node(max_degree_m, 'M' + str(len(M)))
M.insert(0, m1)
plot_degree_distibution(plt, M, next(colors))
u1 = Node(max_degree_u, 'U' + str(len(U)))
U.insert(0, u1)
plot_degree_distibution(plt, U, next(colors))
plt.show()

