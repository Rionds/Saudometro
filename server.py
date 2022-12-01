import http.server
import socketserver

port = 9999

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), handler) as httpd:
    print('Servidor web disponivel na porta ', port)
    httpd.serve_forever()
