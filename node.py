

class Node :
    degree = 0
    label = ""
    prob = 0.0
    cumulative_prob = 0.0
    def __init__(self, degree = 0, label="") :
        self.degree = degree
        self.label = label

    def __eq__(self, other) :
        return self.label == other.label

    def __str__(self) :
        return self.label

    def __hash__(self):
        return hash(('label', self.label, 'degree', self.degree)) 
    
