package main

import "fmt"



type Edge struct {
	To string
	Weight int
}

type Graph struct {
	adjacency map[string][]Edge
	directed bool
}

func NewGraph(directed bool) *Graph {
	return &Graph{
		adjacency: make(map[string][]Edge),
		directed: directed,
	}
}

func (g *Graph) AddVertex(vertex string) {
	if _, exists := g.adjacency[vertex]; !exists {
		g.adjacency[vertex] = []Edge{}
	}
}

func (g *Graph) AddEdge(u, v string, weight int) {
	g.AddVertex(u)
	g.AddVertex(v)
	g.adjacency[u] = append(g.adjacency[u], Edge{To: v, Weight: weight})
}

func (g *Graph) RemoveEdge(u, v string) {
	g.adjacency[u] = filterEdge(g.adjacency[u], v)
}

func filterEdge(edges []Edge, target string) []Edge  {
	filtered := []Edge{}
	for _, edge := range edges {
		if edge.To != target {
			filtered = append(filtered, edge)
		}
	}

	return filtered
}

func (g *Graph) RemoveVertex(vertex string) {
	delete(g.adjacency, vertex)
	for u, edges := range g.adjacency {
		g.adjacency[u] = filterEdge(edges, vertex)
	}
}

func (g *Graph) PrintGraph() {
	for vertex, edges := range g.adjacency {
		fmt.Printf("%s ->", vertex)

		for _, edge := range edges {
			fmt.Printf("%s(%d)", edge.To, edge.Weight)
		}

		fmt.Println()
	}
}

func main() {
	graph := NewGraph(false) // false = undirected

	graph.AddEdge("A", "B", 2)
	graph.AddEdge("A", "C", 3)
	graph.AddEdge("B", "D", 1)
	graph.AddEdge("C", "D", 4)

	graph.RemoveEdge("B", "D")

	graph.PrintGraph()
}
