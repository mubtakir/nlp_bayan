export class KnowledgeGraph {
  nodes: Map<string, any>;
  edges: Array<{from: string; to: string; relation: string}>;

  constructor() {
    this.nodes = new Map();
    this.edges = [];
  }

  addNode(id: string, data: any): void {
    this.nodes.set(id, data);
  }

  addEdge(from: string, to: string, relation: string): void {
    this.edges.push({from, to, relation});
  }
}
