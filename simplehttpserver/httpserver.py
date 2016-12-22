import http.server
import socketserver

PORT = 8001

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("8011", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()
