import cgi
import requests
import urllib.request
import json

print()
#funcion cgi.FieldStorage para que lea los datos ingresados desde la URL
barra_Direcciones = cgi.FieldStorage()
#getvalue para obtener el valor de la URL, se le puse 'name' para que se escriba de la sig manera name=mexico
valor_Barra = barra_Direcciones.getvalue('name')
#URL que es consumido
url = "https://restcountries.eu/rest/v2/name/"
if 'name' not in barra_Direcciones:
	print('''<html>
	<head><title>Countries</title></head>
	<body>
	<h1>No has ingresado ningun valor</h1>
	</body>
	</html>''')
else:
	#se le concatena la url al valor de barra para que este complemente la URL 
	agregando = url+valor_Barra
	# se abre el URL con la funcion open
	urll = urllib.request.urlopen(agregando)
	countryData = urll.read()
	theJSON = json.loads(countryData)
	#para que se vea de manera correcta el JSON
	json_str = json.dumps(theJSON,sort_keys=True, indent=4)
	#se imprime el resultado
	print(json_str)