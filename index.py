# -*- coding: utf-8 -*-
# Author : darren

"""
source env/bin/activate

"""

from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write("DearXuan's API by python!".encode())
        return


print(handler)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(self.headers.get('x-forwarded-for').encode())
        return