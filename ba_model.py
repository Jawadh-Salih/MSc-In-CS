from random import random
from node import Node
from utils import sort_by_degree, create_zipf_nodes, cumulative_prob_dist, create_nodes, get_prob_dict, create_init_graph, create_edge, cal_degree, get_random_user, get_current_degree_probs, insertEdge, get_random_max_prob_movie, plot_degree_distibution, get_alpha_for_degree_dist, tot_degree, wieghted_choice




def BA_Model(M, U, G) :
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
