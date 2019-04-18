'''
Alexander de Jesus Citul Puc
'''
from http.server import HTTPServer, CGIHTTPRequestHandler
class servidor(CGIHTTPRequestHandler):
	cgi_directories = ["/"]

	def handle_http(self,status,content_type,content):

		self.send_response(status)
		self.send_header('Content-type',content_type)
		self.end_headers()

		return bytes(content,'UTF-8')

	def respond(self,result):
	    content = self.handle_http(200, 'application/json',result)
	    self.wfile.write(content)  

if __name__ == '__main__':
	print('Servidor ejecutado...')
	server_address = ('localhost', 8080)
	httpd = HTTPServer(server_address, servidor)
	print('Corriendo servidor...')
	#Try para que cuando se aprete ctrl c el servidor se termine y muestre el mensaje
	try:
	  httpd.serve_forever()
	except KeyboardInterrupt:
	    print('KeyboardInterrupt Ctrl + C')