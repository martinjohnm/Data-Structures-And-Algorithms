





def add_edge(adj, i, j):
    adj[i].add(j)
    adj[j].add(i)

def display_adj_list(adj):
    for i in range(len(adj)):
        print (f'{i}: ', end="")
        for j in adj[i]:
            print(j, end=" ")
        print("")

if __name__ == "__main__":
    v = 4
    adj = [set for _ in range(v)]


    # Now add edges one by one
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 2)
    add_edge(adj, 2, 3)

    print("Adjacency List Representation:")
    display_adj_list(adj)