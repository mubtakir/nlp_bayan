#!/usr/bin/env python3
"""
Bayan Micro-Web Framework Demo
تطبيق ويب مصغر باستخدام بيان

This example demonstrates how to use Bayan's HTTP library and Istinbat Engine
to create a simple API that responds to logical and neural queries.
"""

import sys
import os
import json
import http.server
import socketserver

# Ensure we can import bayan packages
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from bayan.bayan.istinbat_engine import IstinbatEngine
from bayan.bayan.stdlib.http_lib import create_headers

PORT = 9000
ENGINE = IstinbatEngine()

class BayanApiHandler(http.server.BaseHTTPRequestHandler):
    """
    Experimental Micro-Framework Handler
    Handles requests and routes them to Bayan logic
    """
    
    def _send_response(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def do_GET(self):
        if self.path == '/':
            self._send_response({
                "message": "Welcome to Bayan API / مرحبًا بك في واجهة بيان",
                "endpoints": [
                    "/search?q=text (Neural Search)",
                    "/query?q=predicate (Logical Query)",
                    "/stats (System Stats)"
                ]
            })
            return

        if self.path.startswith('/stats'):
            stats = {
                "facts": len(ENGINE.logical_engine.knowledge_base),
                "neural_active": ENGINE.neural_engine.initialized,
                "world": getattr(ENGINE, 'active_world_name', 'Reality')
            }
            self._send_response(stats)
            return

        # Simple Query Parsing
        try:
            from urllib.parse import urlparse, parse_qs
            parsed = urlparse(self.path)
            query_params = parse_qs(parsed.query)
            q = query_params.get('q', [''])[0]

            if parsed.path == '/search':
                # Neural Search
                results = ENGINE.neural_search(q)
                response_data = [
                    {"text": text, "score": score, "fact": str(fact)}
                    for fact, score, text in results
                ]
                self._send_response({"results": response_data})

            elif parsed.path == '/query':
                # Logical Query (simplified)
                # Need to parse predicate string manually or simple lookup
                # For demo, we just echo that logic parsing requires the parser
                self._send_response({"error": "Logical query via API requires Parser integration (Coming Phase 5)"})
            
            else:
                self._send_response({"error": "Not Found"}, 404)

        except Exception as e:
            self._send_response({"error": str(e)}, 500)

def run_app():
    print(f"🚀 Bayan Micro-App running on port {PORT}")
    print(f"Try: http://localhost:{PORT}/search?q=something")
    
    with socketserver.TCPServer(("", PORT), BayanApiHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            httpd.server_close()

if __name__ == "__main__":
    run_app()
