#!/usr/bin/env python3
"""Serve this folder at http://localhost:8638/ (WebAssembly needs http, not file://)."""
import functools
import http.server
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8638
here = os.path.dirname(os.path.abspath(__file__))
handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=here)
handler.extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map,
                          ".wasm": "application/wasm", ".mjs": "text/javascript"}
with http.server.ThreadingHTTPServer(("127.0.0.1", PORT), handler) as server:
    print(f"PEP 638 playground: http://localhost:{PORT}/")
    server.serve_forever()
