

type Edge = { node: string, weight: number }


class Graph {

    private graph : Map<string, Edge[]> = new Map()
    private directed: Boolean = false

    constructor(directed: false) {
        this.directed = directed
    }

    addVertex(vertex: string) {
        if (!this.graph.has(vertex)) {
            this.graph.set(vertex, [])
        }
    }

    addEdge(u: string, v: string, weight: number=1) {

        this.addVertex(u)
        this.addVertex(v)

        this.graph.get(u)!.push({node: v, weight})

        if (!this.directed) {
            this.graph.get(v)!.push({ node: u, weight })
        }

        // this.graph.set(u, (this.graph.get(u) || []).concat(""))

        // if (!this.directed) {
        //     this.graph.set(v, (this.graph.get(v) || []).concat(""))
        // }
    }
 
    removeEdge(u: string, v: string) {
        this.graph.set(
            u, 
            this.graph.get(u)!.filter(edge => edge.node !== v)
        )

        if (!this.directed) {
            this.graph.set(
                v,
                this.graph.get(v)!.filter(edge => edge.node !== u)
            )
        }
    }

    removeVertex(vertex: string) {
        this.graph.delete(vertex);
        for (const [key, edges] of this.graph) {
            this.graph.set(
                key, 
                edges.filter(edge => edge.node !== vertex)
            )
        }
    }

    printGraph() {
        for (const [vertex, edges] of this.graph.entries()) {
          const edgeStr = edges.map(e => `${e.node}(${e.weight})`).join(", ");
          console.log(`${vertex} -> ${edgeStr}`);
        }
      }
   
}


const g = new Graph(false); // false = undirected

g.addEdge("A", "B", 2);
g.addEdge("A", "C", 3);
g.addEdge("B", "D", 1);
g.addEdge("C", "D", 4);

g.removeEdge("B", "D");

g.printGraph();
