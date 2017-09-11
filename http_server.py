
import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('content-type', 'text/html')
		self.end_headers()
		self.wfile.write(('<p>current date: ' + str(datetime.datetime.now().date()) + '</p>\n').encode("utf-8"))
		self.wfile.write(('<p>current time: ' + str(datetime.datetime.now().time()) + '</p>\n').encode("utf-8"))
		return

def main():
	try:
		print('starting http server...')
		server = HTTPServer(('', 8080), MyHandler)
		print('http server started')
		server.serve_forever()
	except KeyboardInterrupt:
		print('exiting...')
		server.socket.close()

if __name__ == '__main__':
	main()

