




# If there is an edge from vertex i to j, mark adjMat[i][j] as 1. 
# If there is no edge from vertex i to j, mark adjMat[i][j] as 0.


def add_edge(mat, i, j):
    # undirected graph
    mat[i][j] = 1
    mat[j][i] = 1

def display_mat(mat):
    for row in mat:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    v = 4 # No of vertices
    mat = [[0] * v for _ in range(v)]

    # Add edges to the graph
    add_edge(mat, 0, 1)
    add_edge(mat, 0, 2)
    add_edge(mat, 1, 2)
    add_edge(mat, 2, 3)

    # Display adjacency matrix
    print("Adjacency Matrix:")
    display_mat(mat)