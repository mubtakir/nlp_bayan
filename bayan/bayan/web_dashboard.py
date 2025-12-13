#!/usr/bin/env python3
"""
Bayan Web Dashboard
لوحة قيادة بيان

A simple web server to visualize the internal state of the Bayan Engine.
Uses standard library http.server to avoid external web framework dependencies.
"""

import http.server
import socketserver
import json
import os
import sys
import threading
import time
import webbrowser
from urllib.parse import urlparse, parse_qs

# Ensure we can import bayan packages
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from bayan.bayan.istinbat_engine import IstinbatEngine
from bayan.bayan.visualization import ExistentialVisualizer

# Global engine instance
ENGINE = None
VISUALIZER = None

PORT = 8080

class BayanRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        if path == '/':
            self.serve_dashboard()
        elif path == '/api/graph':
            self.serve_graph_json()
        elif path == '/api/stats':
            self.serve_stats_json()
        else:
            super().do_GET()

    def serve_dashboard(self):
        """Serve the main HTML dashboard"""
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        html = """
        <!DOCTYPE html>
        <html lang="ar" dir="rtl">
        <head>
            <meta charset="UTF-8">
            <title>Bayan Neural Dashboard | لوحة قيادة بيان</title>
            <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
            <style>
                body { font-family: 'Segoe UI', sans-serif; margin: 0; padding: 0; background: #f0f2f5; }
                header { background: #2c3e50; color: white; padding: 1rem; text-align: center; }
                .container { display: flex; flex-wrap: wrap; padding: 20px; gap: 20px; }
                .card { background: white; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); flex: 1; min-width: 300px; }
                .full-width { flex: 100%; }
                h2 { color: #2c3e50; border-bottom: 2px solid #eee; padding-bottom: 10px; }
                .stat-box { text-align: center; font-size: 2em; font-weight: bold; color: #3498db; }
                .stat-label { text-align: center; color: #7f8c8d; }
                #mermaid-graph { overflow-x: auto; }
            </style>
        </head>
        <body>
            <header>
                <h1>🧠 Bayan Neuro-Symbolic Dashboard</h1>
                <p>لوحة التحكم العصبية-الرمزية</p>
            </header>
            
            <div class="container">
                <!-- Stats -->
                <div class="card">
                    <div class="stat-box" id="fact-count">-</div>
                    <div class="stat-label">Facts (حقائق)</div>
                </div>
                <div class="card">
                    <div class="stat-box" id="world-name">-</div>
                    <div class="stat-label">Active World (العالم النشط)</div>
                </div>
                <div class="card">
                    <div class="stat-box" id="engine-mode">Hybrid</div>
                    <div class="stat-label">Mode (النمط)</div>
                </div>
            </div>

            <div class="container">
                <!-- Knowledge Graph -->
                <div class="card full-width">
                    <h2>Knowledge Graph (الخريطة المعرفية)</h2>
                    <div id="mermaid-graph" class="mermaid">
                        graph TD;
                        Loading...
                    </div>
                    <button onclick="loadGraph()">Refresh Graph / تحديث</button>
                </div>
            </div>

            <script>
                mermaid.initialize({ startOnLoad: true });

                async function fetchStats() {
                    const response = await fetch('/api/stats');
                    const data = await response.json();
                    document.getElementById('fact-count').innerText = data.fact_count;
                    document.getElementById('world-name').innerText = data.active_world;
                }

                async function loadGraph() {
                    const response = await fetch('/api/graph');
                    const data = await response.json();
                    
                    const element = document.getElementById('mermaid-graph');
                    // Simple conversion of nodes/links to Mermaid syntax for demo purposes
                    // In a real app, we'd use D3.js or Cytoscape, but Mermaid is easier related to existing viz code
                    let mermaidCode = "graph TD;\\n";
                    
                    data.nodes.forEach(n => {
                        let shape = n.type === 'concept' ? '([' + n.label + '])' : '[' + n.label + ']';
                        mermaidCode += `    ${n.id}${shape}\\n`;
                    });
                    
                    data.links.forEach(l => {
                        mermaidCode += `    ${l.source} -->|${l.relationship}| ${l.target}\\n`;
                    });

                    element.removeAttribute('data-processed');
                    element.innerHTML = mermaidCode;
                    mermaid.run({ nodes: [element] });
                }

                // Init
                fetchStats();
                loadGraph();
                setInterval(fetchStats, 5000); // Auto-refresh stats
            </script>
        </body>
        </html>
        """
        self.wfile.write(html.encode('utf-8'))

    def serve_stats_json(self):
        """API: Return engine statistics"""
        stats = {
            'fact_count': len(ENGINE.logical_engine.knowledge_base),
            'active_world': getattr(ENGINE, 'active_world_name', 'Reality'),
            'neural_status': 'Active' if ENGINE.neural_engine.initialized else 'Fallback'
        }
        self.send_json(stats)

    def serve_graph_json(self):
        """API: Return graph data from visualizer"""
        # Using the existing export_d3_graph method from visualization.py
        graph_data = VISUALIZER.export_d3_graph()
        self.send_json(graph_data)

    def send_json(self, data):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

def start_server():
    global ENGINE, VISUALIZER
    print("🔌 Starting Bayan Dashboard Server...")
    
    # Initialize Engine suitable for visualization
    ENGINE = IstinbatEngine()
    
    # Add some dummy data to visualize if empty
    from bayan.bayan.logical_engine import Fact, Predicate, Term
    if not ENGINE.logical_engine.knowledge_base:
        ENGINE.logical_engine.add_fact(Fact(Predicate("is_system", [Term("Bayan")])))
        ENGINE.logical_engine.add_fact(Fact(Predicate("has_component", [Term("Bayan"), Term("Dashboard")])))
        ENGINE.logical_engine.add_fact(Fact(Predicate("has_component", [Term("Bayan"), Term("LogicEngine")])))
        ENGINE.logical_engine.add_fact(Fact(Predicate("connected_to", [Term("LogicEngine"), Term("NeuralEngine")])))

    # Initialize Visualizer (mocking interpreter interface since Visualizer expects one)
    class MockInterpreter:
        def __init__(self, engine):
            self.logical_engine = engine.logical_engine
            # Stub other attrs expected by visualizer
            self._domains = {}
            self._environments = {}
            self._existential_beings = {}
            self._domain_relations = {}
            self._domain_actions = {}
            self._domain_laws = {}
            self.logical = engine.logical_engine

    mock_interpreter = MockInterpreter(ENGINE)
    VISUALIZER = ExistentialVisualizer(mock_interpreter)

    print(f"✅ Server running at http://localhost:{PORT}")
    
    with socketserver.TCPServer(("", PORT), BayanRequestHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            httpd.server_close()

if __name__ == "__main__":
    start_server()
