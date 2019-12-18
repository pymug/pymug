import socket
import http.server
import socketserver
import webbrowser

# tasklist
# /IM py37.exe /F
# 
hostname = socket.gethostname()
PORT = 8000
IP = socket.gethostbyname(hostname)


Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print('serving on:')
    link = 'http://{}:{}'.format(IP, PORT)
    print(link)
    webbrowser.open(link)
    httpd.serve_forever()

