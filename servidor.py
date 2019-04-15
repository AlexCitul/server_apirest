'''
Alexander de Jesus Citul Puc
'''
from http.server import HTTPServer, CGIHTTPRequestHandler
# Solicitudes HTTP
class servidor(CGIHTTPRequestHandler):
  
  cgi_directories = ["/"]
      
def run():
  print('Servidor ejecutado...')
  # configuración del servidor
  # Nombre y puerto para iniciar el servidor
  server_address = ('localhost', 8080)
  httpd = HTTPServer(server_address, servidor)
  print('Corriendo servidor...')
  #Try para que cuando se aprete ctrl c el servidor se termine y muestre el mensaje
  try:
      httpd.serve_forever()
  except KeyboardInterrupt:
        print('KeyboardInterrupt Ctrl + C')
 
run()