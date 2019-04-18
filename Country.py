import cgi
import requests
import urllib.request
import json
class Country():

	def __init__(self,url):
		print()
		barra_Direcciones = cgi.FieldStorage()
		valor_Barra = barra_Direcciones.getvalue('name')
		self.url = url
		if 'name' not in barra_Direcciones:
			print('''<html>
			<head><title>Countries</title></head>
			<body>
			<h1>No has ingresado ningun valor</h1>
			</body>
			</html>''')
		else:
			#se le concatena la url al valor de barra para que este complemente la URL 
			agregando = self.url+valor_Barra
			# se abre el URL con la funcion open
			urll = urllib.request.urlopen(agregando)
			countryData = urll.read()
			theJSON = json.loads(countryData)
			#para que se vea de manera correcta el JSON
			json_str = json.dumps(theJSON,sort_keys=True, indent=4)
			#se imprime el resultado
			print(json_str)
			
if __name__ == '__main__':
	link = Country("https://restcountries.eu/rest/v2/name/")
	



