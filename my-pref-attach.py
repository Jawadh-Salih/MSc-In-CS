from random import randint
from utils import create_nodes, create_init_graph, tot_degree, plot_degree_distibution
from graph import Graph
# Create a set of M nodes
M = create_nodes('M', randint(900, 1000))
# Create a set of U nodes
U = create_nodes('U', randint(9000, 10000))

# Now there isn't a competition. So Movies can be viewed by infinite number of users.
# This is against the given definition of Zipf's Law, which states there is scarcity of the sharing resources.
# But for our scenario we have used time as a scarce resources. 

# Now create a Graph with set of nodes connected in a bipartite way
G = Graph(M, U)
create_init_graph(M, U, G)



G.print_degree_dist(M)
# plot_degree_distibution(M)
# plot_degree_distibution(U)